# Generated by Django 5.0.1 on 2024-01-16 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synergy', '0009_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='users/profile.jpg', upload_to='users/'),
        ),
    ]
