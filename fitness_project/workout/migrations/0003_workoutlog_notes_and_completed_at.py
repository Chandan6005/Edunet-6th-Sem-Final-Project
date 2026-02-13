# Generated migration for WorkoutLog model updates

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_workoutlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutlog',
            name='notes',
            field=models.TextField(blank=True, help_text='Optional notes about your workout', null=True),
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
