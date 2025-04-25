# analytics/management/commands/run_analysis.py
from django.core.management.base import BaseCommand
from django.db.models import Count
from apps.documents.models import Document
import pandas as pd
from pathlib import Path
from django.conf import settings

class Command(BaseCommand):
    help = "Generate Excel report 'documents per process'"

    def handle(self, *args, **kwargs):
        data = (Document.objects
                .values('process__name')
                .annotate(total=Count('id'))
                .order_by('-total'))
        df = pd.DataFrame.from_records(data)
        reports_dir = Path(settings.MEDIA_ROOT) / 'reports'
        reports_dir.mkdir(parents=True, exist_ok=True)
        out = reports_dir / 'report.xlsx'
        df.to_excel(out, index=False)
        self.stdout.write(self.style.SUCCESS(f'✓ Report saved to {out}'))
