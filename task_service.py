from datetime import datetime, timedelta
from models import Task
from tag_service import get_or_create_tag


def parse_date_safe(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None


def is_future_enough(date_obj):
    return date_obj > datetime.now() + timedelta(minutes=1)


def validate_due_date(due):
    due_date = parse_date_safe(due)

    if not due_date:
        print("Invalid date format. Use YYYY-MM-DD.")
        return None

    if not is_future_enough(due_date):
        print("Due date must be in the future.")
        return None

    return due_date


def create_task(session, title, desc, priority, due_date, user_id, project_id, tags):

    task = Task(
        title=title,
        description=desc,
        status="todo",
        priority=priority,
        due_date=due_date,
        user_id=user_id,
        project_id=project_id
    )

    for t in tags:
        t = t.strip()
        if t:
            task.tags.append(get_or_create_tag(session, t))

    session.add(task)
    session.commit()
    return True


def list_tasks(session, user_id):
    return session.query(Task).filter_by(user_id=user_id).all()


def mark_done(session, task_id):
    task = session.get(Task, task_id)
    if task:
        task.status = "done"
        session.commit()
