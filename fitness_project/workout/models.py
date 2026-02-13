from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Workout(models.Model):
    GOAL_CHOICES = [
        ('lose_weight', 'Lose Weight'),
        ('gain_muscle', 'Gain Muscle'),
        ('maintain', 'Maintain Fitness'),
    ]

    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    exercise = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Minutes")
    calories_burn = models.IntegerField()

    def __str__(self):
        return self.exercise
    
class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_day = models.IntegerField()
    date = models.DateField(default=date.today)
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True, help_text="Optional notes about your workout")
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - Day {self.workout_day} - {self.date}"