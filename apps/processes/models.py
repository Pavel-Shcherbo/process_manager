
from django.db import models

class Process(models.Model):
    branch = models.ForeignKey('branches.Branch', models.CASCADE, related_name='processes')
    name = models.CharField(max_length=255)
    level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.branch}: {self.name}'

class ProcessRelation(models.Model):
    process = models.ForeignKey(Process, models.CASCADE, related_name='children_rel')
    sub_process = models.ForeignKey(Process, models.CASCADE, related_name='parent_rel')

    class Meta:
        unique_together = ('process', 'sub_process')
