# Generated by Django 5.0.1 on 2024-01-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synergy', '0004_alter_profile_avatar_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='profile.jpg', null=True, upload_to=''),
        ),
    ]
