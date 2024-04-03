# Generated by Django 4.2.7 on 2024-04-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lexicon_App', '0002_rename_course_name_course_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='github_profile',
            new_name='github_ID',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='linkedin_profile',
            new_name='linkedin_ID',
        ),
        migrations.RemoveField(
            model_name='student',
            name='language_proficiency',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='portfolio_profile',
        ),
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='confirm_password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='User Email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
