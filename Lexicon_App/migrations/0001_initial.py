# Generated by Django 5.0.3 on 2024-03-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseID', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('social_security_number', models.CharField(max_length=20)),
                ('postal_address', models.CharField(max_length=200)),
                ('knowledge_level', models.CharField(max_length=100)),
                ('GDPR_consent', models.BooleanField(default=False)),
                ('language_proficiency', models.CharField(max_length=200)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv/')),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
                ('github_profile', models.URLField(blank=True, null=True)),
                ('portfolio_profile', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyID', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('accepting_interns', models.BooleanField(default=False)),
                ('openings_job_description', models.TextField(blank=True)),
                ('contact_details', models.ManyToManyField(to='Lexicon_App.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='student_ID',
            field=models.ManyToManyField(to='Lexicon_App.student'),
        ),
    ]
