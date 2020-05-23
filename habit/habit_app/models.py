from django.db import models
from datetime import date
# Create your models here.


class Habit(models.Model):
    title = models.CharField(blank=False, max_length=50, unique=True)
    description = models.TextField(max_length=150)
    start_date = models.DateField()
    reason = models.TextField(blank=True)
    plan = models.TextField(blank=True)


class Progress(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    rating = models.IntegerField(default=10)
    edit_date = models.DateField()
    feeling = models.TextField()
