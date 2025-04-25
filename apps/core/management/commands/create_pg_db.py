
import os, subprocess
from django.core.management.base import BaseCommand, CommandError
class Command(BaseCommand):
    help = 'Create PostgreSQL role and database'

    def add_arguments(self, parser):
        parser.add_argument('--superuser', required=True)
        parser.add_argument('--superpass', required=True)

    def handle(self, *args, **opts):
        db = os.getenv('POSTGRES_DB')
        user = os.getenv('POSTGRES_USER')
        pwd = os.getenv('POSTGRES_PASSWORD')
        host = os.getenv('POSTGRES_HOST', 'localhost')
        port = os.getenv('POSTGRES_PORT', '5432')
        superuser = opts['superuser']
        superpass = opts['superpass']
        try:
            subprocess.run([
                'psql', f'-U{superuser}', f'-h{host}', '-p', port,
                '-c', f"CREATE ROLE {user} WITH LOGIN PASSWORD '{pwd}'"
            ], check=False)
            subprocess.run([
                'psql', f'-U{superuser}', f'-h{host}', '-p', port,
                '-c', f"CREATE DATABASE {db} OWNER {user}"
            ], check=True)
            self.stdout.write(self.style.SUCCESS('Database and role created'))
        except Exception as e:
            raise CommandError(str(e))
