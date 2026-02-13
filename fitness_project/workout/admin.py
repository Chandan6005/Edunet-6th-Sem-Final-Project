from django.contrib import admin
from .models import Workout, WorkoutLog

# Register your models here.

admin.site.register(Workout)

@admin.register(WorkoutLog)
class WorkoutLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'workout_day', 'date', 'completed', 'completed_at')
    list_filter = ('completed', 'date', 'workout_day')
    search_fields = ('user__username', 'notes')
    readonly_fields = ('completed_at',)
    fieldsets = (
        ('Workout Information', {
            'fields': ('user', 'workout_day', 'date')
        }),
        ('Completion Status', {
            'fields': ('completed', 'completed_at', 'notes')
        }),
    )
