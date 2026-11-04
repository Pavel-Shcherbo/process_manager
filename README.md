# Process Manager

Web system for managing business processes and the documents that belong to them. Built with Django and PostgreSQL. The interface is a set of server-rendered pages with a dashboard, a process tree and document lists.

## Features

- Companies and branches
- Users with three roles: super admin, admin, user (each user can belong to a branch)
- Business processes with a hierarchy (parent and sub-processes) and a responsible person
- Documents attached to a process: policy, instruction, regulation, other, with file upload and signing date
- Dashboard, process tree view, list and detail pages
- `run_analysis` management command for analytics (pandas, openpyxl)
- Demo data fixture (`demo.json`)

## Stack

Python, Django 4.2, PostgreSQL (psycopg2), pandas, openpyxl, HTML templates

## Project structure

```
apps/        Django apps: companies, branches, users, processes, documents, staff, core
config/      settings, urls, wsgi / asgi
templates/   HTML templates
analytics/   analysis script
demo.json    sample data
```

## Quick start

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

export DEBUG=True
export POSTGRES_DB=process_manager_db
export POSTGRES_USER=process_manager_user
export POSTGRES_PASSWORD=<choose a password>
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432

python manage.py create_pg_db --superuser postgres --superpass <postgres admin password>
python manage.py migrate
python manage.py loaddata demo.json
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ and sign in with the user you created.

## Notes

- Database settings are read from environment variables. Keep them out of git (`.env` is in `.gitignore`).
- `create_pg_db` creates the PostgreSQL database and user for you.

## Author

Pavel Shcherbo
