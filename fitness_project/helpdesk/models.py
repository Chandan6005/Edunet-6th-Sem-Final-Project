from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Reminder(models.Model):
    REMINDER_TYPES = [
        ('workout', 'Workout Reminder'),
        ('diet', 'Diet Reminder'),
        ('checkin', 'Check-in Reminder'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('dismissed', 'Dismissed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reminders')
    reminder_type = models.CharField(max_length=20, choices=REMINDER_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reminder_date = models.DateField(default=date.today)
    
    class Meta:
        ordering = ['-reminder_date', '-created_at']
    
    def __str__(self):
        return f"{self.get_reminder_type_display()} - {self.user.username} ({self.status})"
