from rich.console import Console
from task_service import create_task, list_tasks, mark_done
from project_service import create_project, list_projects
from stats_service import get_stats
from export_import import export_csv

console = Console()

def main_menu():
    console.print("\n1) Create Task")
    console.print("2) List Tasks")
    console.print("3) Mark Task As Done")
    console.print("4) Statistics")
    console.print("5) Export CSV")
    console.print("6) Exit")
    return input("> ")


def show_tasks(tasks):
    if not tasks:
        console.print("No tasks found.")
        return

    console.print("\nID | Title | Status | Priority | Due Date  | Description")
    console.print("-" * 60)

    for t in tasks:
        console.print(
            f"{t.id} | {t.title} | {t.status} | "
            f"{t.priority} | {t.due_date} "
            f"| {t.description}"
        )
