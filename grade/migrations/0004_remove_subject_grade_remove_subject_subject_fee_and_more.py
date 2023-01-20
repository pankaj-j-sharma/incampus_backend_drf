# Generated by Django 4.1.5 on 2023-01-20 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_alter_teachersalary_teacher'),
        ('grade', '0003_subject_grade_subject_subject_fee_subject_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject_fee',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.CreateModel(
            name='SubjectRouting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('subject_fee', models.FloatField(blank=True, null=True)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade.grade')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.incampusteacher')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]