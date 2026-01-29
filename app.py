from db import Base, engine, SessionLocal
from auth import register, login
from cli import main_menu, show_tasks
from project_service import create_project
from stats_service import get_stats
from export_import import export_csv
from task_service import create_task, list_tasks, mark_done, validate_due_date

Base.metadata.create_all(engine)
session = SessionLocal()

MAX_TRIES = 3
user = None

print("1) Register")
print("2) Login")

mode = input("> ")

tries = 0

while tries < MAX_TRIES and not user:
    username = input("Username: ")
    password = input("Password: ")

    if mode == "1":
        user = register(session, username, password)
    else:
        user = login(session, username, password)

    if not user:
        tries += 1
        remaining = MAX_TRIES - tries
        if remaining > 0:
            print(f"Invalid credentials. Attempts left: {remaining}")
        else:
            print("Too many failed attempts. Exiting.")
            exit()

# =========================
# MAIN LOOP
# =========================

while True:
    c = main_menu()

    if c == "1":
        title = input("Title: ").strip()
        if not title:
            print("Title cannot be empty.")
            continue

        desc = input("Desc: ")
        try:
            pr = int(input("Priority(1-5): "))
            if pr < 1 or pr > 5:
                raise ValueError
        except ValueError:
            print("Priority must be number between 1 and 5.")
            continue


        proj = create_project(session, "Default", user.id)


        due_input = input("Due (YYYY-MM-DD): ")
        due_date = validate_due_date(due_input)

        if not due_date:
            continue

        tags = input("Tags comma separated: ").split(",")

        proj = create_project(session, "Default", user.id)

        create_task(
            session,
            title,
            desc,
            pr,
            due_date,
            user.id,
            proj.id,
            tags
        )



    elif c == "2":
        show_tasks(list_tasks(session, user.id))


    elif c == "3":

        tasks = list_tasks(session, user.id)

        show_tasks(tasks)

        task_id = input("\nEnter task ID to mark as done: ")

        if task_id.isdigit():

            mark_done(session, int(task_id))

            print("Task marked as done.")

        else:

            print("Invalid task id.")



    elif c == "4":
        t, d, p = get_stats(session, user.id)
        print(f"Total:{t} Done:{d} Pending:{p}")


    elif c == "5":

        success, message = export_csv(session, user.id, "tasks.csv")

        print(message)


    elif c == "6":
        print("Goodbye.")
        break
