from django.urls import path
from .views import dismiss_reminder, mark_reminder_completed, view_all_reminders

urlpatterns = [
    path('reminders/', view_all_reminders, name='view_reminders'),
    path('reminders/<int:reminder_id>/dismiss/', dismiss_reminder, name='dismiss_reminder'),
    path('reminders/<int:reminder_id>/complete/', mark_reminder_completed, name='complete_reminder'),
]
