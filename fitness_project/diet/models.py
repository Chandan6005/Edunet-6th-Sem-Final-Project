from django.db import models

# Create your models here.
class Diet(models.Model):
    GOAL_CHOICES = [
        ('lose_weight', 'Lose Weight'),
        ('gain_muscle', 'Gain Muscle'),
        ('maintain', "Maintain Weight"),
    ]

    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)
    food = models.CharField(max_length=100)
    calories = models.IntegerField()

    def __str__(self):
        return self.food