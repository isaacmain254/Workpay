# Generated by Django 4.2.4 on 2023-09-15 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_remove_job_required_skill_job_required_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='required_skill',
            new_name='required_skills',
        ),
    ]
