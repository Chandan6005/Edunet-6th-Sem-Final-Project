from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.utils import timezone
from workout.models import Workout
from workout.ml_utils import predict_workout_level
from dashboard.utils import calculate_bmi
from .ai_utils import generate_workout_plan
from datetime import date, timedelta
from .models import WorkoutLog
from .utils import calculate_streak
from helpdesk.models import Reminder
# Create your views here.

@login_required
def workout_view(request):
    profile = request.user.profile
    RAW_GOAL = profile.goal or 'maintain'

    GOAL_MAP = {
        'Weight loss': 'lose',
        'Weight gain': 'gain',
        'Maintain': 'maintain',
        'lose': 'lose',
        'gain': 'gain',
        'maintain': 'maintain',
    }

    goal = GOAL_MAP.get(RAW_GOAL, 'maintain')
    
    age = profile.age or 25
    height = profile.height or 170
    weight = profile.weight or 70

    bmi = None
    if profile.height and profile.weight:
        bmi = calculate_bmi(profile.height, profile.weight)
    else:
        bmi = 22
    
    level = predict_workout_level(age, height, weight, bmi, goal)
    cache_key = f"workout_{request.user.id}_{goal}_{level}"
    ai_workout_plan = cache.get(cache_key)
    
    if not ai_workout_plan:
        ai_workout_plan = generate_workout_plan(profile, level, goal)
        cache.set(cache_key, ai_workout_plan,  timeout=3600)

    today = date.today()
    days_since_join = (today - request.user.date_joined.date()).days
    current_day = (days_since_join % 7) + 1

    log, created = WorkoutLog.objects.get_or_create(
        user=request.user,
        workout_day=current_day,
        date=today
    )

    if request.method == "POST" and "complete_workout" in request.POST:
        log.completed = True
        log.completed_at = timezone.now()
        
        # Get optional notes if provided
        workout_notes = request.POST.get('workout_notes', '').strip()
        if workout_notes:
            log.notes = workout_notes
        
        log.save()
        
        # Mark reminder as completed
        Reminder.objects.filter(
            user=request.user,
            reminder_type='workout',
            reminder_date=today,
            status='pending'
        ).update(status='completed')

    tomorrow_day = (current_day % 7) + 1
    streak = calculate_streak(request.user)

    return render(request, 'workout.html', {
        'ai_workout_plan': ai_workout_plan,
        'current_day': current_day,
        "completed": log.completed,
        "tomorrow_day": tomorrow_day,
        "streak": streak,
        "level": level,
    })

