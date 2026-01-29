import csv
from models import Task

def export_csv(session, user_id, filename):
    try:
        tasks = session.query(Task).filter_by(user_id=user_id).all()

        if not tasks:
            return False, "No tasks to export."

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["id", "title", "status", "priority", "due_date", "description"]
            )

            for t in tasks:
                writer.writerow([
                    t.id,
                    t.title,
                    t.status,
                    t.priority,
                    t.due_date,
                    t.description
                ])

        return True, f"Exported {len(tasks)} tasks to {filename}"

    except Exception as e:
        return False, f"Export failed: {str(e)}"

def import_csv(session, filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
