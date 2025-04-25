
import pandas as pd
from django.core.management.base import BaseCommand
from apps.documents.models import Document
from django.conf import settings
from pathlib import Path

class Command(BaseCommand):
    help = 'Generate Excel report'

    def handle(self, *args, **kwargs):
        qs = Document.objects.values('process__name', 'doc_type').annotate(cnt=pd.Count('id'))
        df = pd.DataFrame.from_records(qs)
        reports_dir = Path(settings.MEDIA_ROOT) / 'reports'
        reports_dir.mkdir(parents=True, exist_ok=True)
        path = reports_dir / 'report.xlsx'
        df.to_excel(path, index=False)
        self.stdout.write(self.style.SUCCESS(f'Report saved to {path}'))
