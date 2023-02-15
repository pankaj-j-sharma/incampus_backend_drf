# Generated by Django 4.1.5 on 2023-02-12 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_incampususer_address_incampususer_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='incampususer',
            name='about_me',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='incampususer',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='incampususer',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='incampususer',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='incampususer',
            name='job',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='incampususer',
            name='postal_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]