# Generated by Django 4.1.5 on 2023-03-01 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0007_classroom_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dailytimetable',
            unique_together={('schedule_day', 'start_time', 'grade')},
        ),
    ]
