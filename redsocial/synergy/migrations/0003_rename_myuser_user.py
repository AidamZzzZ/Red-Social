# Generated by Django 5.0.1 on 2024-01-13 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('synergy', '0002_myuser_profile_delete_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUser',
            new_name='User',
        ),
    ]
