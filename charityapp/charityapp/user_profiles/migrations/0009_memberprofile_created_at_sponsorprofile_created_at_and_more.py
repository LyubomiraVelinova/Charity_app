# Generated by Django 4.2.3 on 2023-07-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0008_remove_memberprofile_contribution_history_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberprofile',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sponsorprofile',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volunteerprofile',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
