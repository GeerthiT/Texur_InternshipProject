# Generated by Django 5.0.3 on 2024-03-25 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lexicon_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_name',
            new_name='name',
        ),
    ]
