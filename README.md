
# Process Manager

Корпоративная система управления процессами и документами.

## Быстрый старт

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# .env (пример)
export DEBUG=True
export POSTGRES_DB=process_manager_db
export POSTGRES_USER=process_manager_user
export POSTGRES_PASSWORD=process_manager_pass
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432

python manage.py create_pg_db --superuser postgres --superpass <pwd>
python manage.py migrate
python manage.py loaddata demo.json
python manage.py runserver
```

Зайдите на http://127.0.0.1:8000/  
Пользователь SUPERADMIN: `super`, пароль задайте через `createsuperuser` или измените в админке.
