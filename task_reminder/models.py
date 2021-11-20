from django.db import models

# Create your models here.

class TodoTask(models.Model):
    reminder_date = models.DateTimeField()
    task_name = models.CharField(max_length=100)
    task_description = models.CharField(max_length=250)
    email = models.EmailField()
