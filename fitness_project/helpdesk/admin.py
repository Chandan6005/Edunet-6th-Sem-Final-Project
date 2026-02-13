from django.contrib import admin
from .models import Reminder

# Register your models here.

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('user', 'reminder_type', 'title', 'status', 'reminder_date')
    list_filter = ('status', 'reminder_type', 'reminder_date')
    search_fields = ('user__username', 'title', 'description')
    readonly_fields = ('created_at', 'updated_at')

