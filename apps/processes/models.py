from django.db import models
from django.conf import settings

class Process(models.Model):
    branch = models.ForeignKey('branches.Branch', models.CASCADE, related_name='processes')
    name = models.CharField(max_length=255)
    level = models.PositiveIntegerField(default=0)
    responsible = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.SET_NULL,
        null=True,
        blank=True,
        related_name='responsible_processes'
    )

    def __str__(self):
        return self.name

class ProcessRelation(models.Model):
    process = models.ForeignKey(Process, models.CASCADE, related_name='children_rel')
    sub_process = models.ForeignKey(Process, models.CASCADE, related_name='parent_rel')

    class Meta:
        unique_together = ('process', 'sub_process')