from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reminder

# Create your views here.

@login_required
def dismiss_reminder(request, reminder_id):
    """Dismiss a specific reminder"""
    reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)
    reminder.status = 'dismissed'
    reminder.save()
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))


@login_required
def mark_reminder_completed(request, reminder_id):
    """Mark a reminder as completed"""
    reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)
    reminder.status = 'completed'
    reminder.save()
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))


@login_required
def view_all_reminders(request):
    """View all reminders for the current user"""
    reminders = Reminder.objects.filter(user=request.user).order_by('-reminder_date', '-created_at')
    
    context = {
        'reminders': reminders,
        'pending': reminders.filter(status='pending').count(),
        'completed': reminders.filter(status='completed').count(),
        'dismissed': reminders.filter(status='dismissed').count(),
    }
    
    return render(request, 'reminders.html', context)

