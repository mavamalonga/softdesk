# Generated by Django 4.0 on 2022-01-04 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_contributor_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='projet_type',
            new_name='project_type',
        ),
    ]