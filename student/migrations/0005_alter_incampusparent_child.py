# Generated by Django 4.1.5 on 2023-01-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_incampusparent_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incampusparent',
            name='child',
            field=models.ManyToManyField(to='student.incampusstudent'),
        ),
    ]