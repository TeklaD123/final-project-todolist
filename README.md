Smart Todo CLI Application Project Description

Smart Todo is a command-line based task management system written in Python. It allows users to register, log in, and manage their personal tasks with persistence, validation, and statistics.

The system supports:

User authentication

Task creation with validation

Task listing

Marking tasks as completed

Task statistics

CSV export

Persistent storage using SQLite

The project demonstrates modular design, data modeling, validation, and separation of concerns.

Features

User registration and login

Password hashing using bcrypt

Create tasks with:

Title

Description

Priority (1–5)

Due date (validated)

Tags

List all tasks

Mark tasks as done

View statistics:

Total tasks

Completed tasks

Pending tasks

Export tasks to CSV file

Input validation and error handling

Persistent SQLite database

Architecture Overview 
smart_todo/ 
├── app.py # Application entry point 
├── db.py # Database connection 
├── models.py # SQLAlchemy models 
├── auth.py # Authentication logic 
├── task_service.py # Task business logic 
├── project_service.py # Project logic 
├── tag_service.py # Tag logic 
├── stats_service.py # Statistics 
├── export_import.py # CSV export/import 
├── cli.py # Menus and display 
├── requirements.txt 
└── smart_todo.db # Created automatically

Architecture follows layered design:



CLI layer → User interaction

Service layer → Business logic

Model layer → Database schema

Database Model

Entities:

User

Project

Task

Tag

TaskTag (many-to-many)

Relationships:

User → Tasks

User → Projects

Project → Tasks

Task ↔ Tags

Technologies Used

Python 3.10+

SQLite

SQLAlchemy ORM

bcrypt

rich

How to Run

Clone repository git clone <your-repo-url> cd smart_todo

Create virtual environment (optional but recommended) python -m venv venv

Windows:

venv\Scripts\activate

Linux / Mac:

source venv/bin/activate

Install dependencies pip install -r requirements.txt

Run application python app.py

Example Menu

Create Task
List Tasks
Mark Task As Done
Statistics
Export CSV
Exit
CSV Export

When option 5 is selected, file tasks.csv is generated in the project folder.

Columns:

id, title, status, priority, due_date, description

Known Limitations

CLI interface only (no GUI)

Single-machine database

No task editing or deletion

No search/filter by tags or priority

Possible Future Improvements

Task editing and deletion

Search and filtering

Sorting by priority or due date

Task reminders

Web version (Flask/FastAPI)

Role-based permissions

AI Tool Usage

ChatGPT was used as an assisting tool for:

Architecture suggestions

Debugging assistance

Code improvement ideas

All code was reviewed, understood, and adapted by the author.

Author

Tekla Durglishvili # final-project-todo-list # final-project-todo-list
