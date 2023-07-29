from django.db import models

# Create your models here.
class TasksInfo(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    due_date = models.CharField(max_length=50)
    priority_levels = models.CharField(max_length=10)
    status = models.CharField(max_length=20)