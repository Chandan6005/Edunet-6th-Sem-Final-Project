from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.utils import calculate_bmi, bmi_category
from workout.models import WorkoutLog
from helpdesk.models import Reminder
from datetime import date, timedelta

@login_required
def dashboard_view(request):
    profile = request.user.profile

    bmi = None
    category = "Update your profile to calculate BMI"

    if profile.weight and profile.height:
        bmi = calculate_bmi(profile.weight, profile.height)
        category = bmi_category(bmi)

    # Get workout logs for the current week
    today = date.today()
    days_since_join = (today - request.user.date_joined.date()).days
    current_day = (days_since_join % 7) + 1
    
    # Get the past 7 days of workout logs
    week_start = today - timedelta(days=6)
    week_logs = WorkoutLog.objects.filter(
        user=request.user,
        date__gte=week_start
    ).order_by('date')
    
    # Create or get reminders for this week
    reminders = Reminder.objects.filter(
        user=request.user,
        reminder_type='workout',
        reminder_date__gte=week_start
    ).order_by('-reminder_date')
    
    # Count completed and pending workouts
    completed_count = week_logs.filter(completed=True).count()
    pending_count = week_logs.filter(completed=False).count()
    
    # Get today's workout status
    today_log = WorkoutLog.objects.filter(
        user=request.user,
        date=today
    ).first()
    
    # Create reminder for today if workout not completed
    if today_log and not today_log.completed:
        reminder, created = Reminder.objects.get_or_create(
            user=request.user,
            reminder_type='workout',
            reminder_date=today,
            defaults={
                'title': f'Complete Today\'s Workout - Day {today_log.workout_day}',
                'description': f'You have not completed your workout for today. Keep your streak going!',
                'status': 'pending'
            }
        )
    elif today_log and today_log.completed:
        # Mark reminder as completed if workout is done
        Reminder.objects.filter(
            user=request.user,
            reminder_type='workout',
            reminder_date=today
        ).update(status='completed')

    context = {
        'bmi': bmi,
        'category': category,
        'goal': profile.goal,
        'weight': profile.weight,
        'height': profile.height,
        'week_logs': week_logs,
        'reminders': reminders,
        'completed_count': completed_count,
        'pending_count': pending_count,
        'today_log': today_log,
        'current_day': current_day,
    }

    return render(request,'dashboard.html', context)
