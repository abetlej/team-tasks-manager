# Generated by Django 3.1 on 2020-08-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_tasks_managers', '0003_auto_20200814_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('in_progress', 'in progress'), ('completed', 'completed'), ('not_completed', 'not completed')], default='not_completed', max_length=20),
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
