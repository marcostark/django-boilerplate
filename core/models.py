from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone


class Task(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.description

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now