# Generated by Django 4.2.3 on 2023-08-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0014_remove_donationcampaign_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationcampaign',
            name='logo',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
