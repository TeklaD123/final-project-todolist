from models import Task

def get_stats(session, user_id):
    total = session.query(Task).filter_by(user_id=user_id).count()
    done = session.query(Task).filter_by(user_id=user_id, status="done").count()
    return total, done, total - done
