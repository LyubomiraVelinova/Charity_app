# Generated by Django 4.2.3 on 2023-08-05 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0002_alter_memberprofile_options_and_more'),
        ('work', '0003_rename_charitycampaigns_charitycampaign'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DonationCampaigns',
            new_name='DonationCampaign',
        ),
    ]
