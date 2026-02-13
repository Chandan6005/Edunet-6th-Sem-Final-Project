from datetime import date, timedelta
from .models import WorkoutLog

def calculate_streak(user):
    streak = 0
    today = date.today()

    while True:
        log = WorkoutLog.objects.filter(
            user=user,
            date=today,
            completed=True
        ).first()

        if log:
            streak += 1
            today -= timedelta(days=1)
        else:
            break
    return streak