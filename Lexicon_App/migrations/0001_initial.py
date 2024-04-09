# Generated by Django 5.0.3 on 2024-04-08 12:07

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
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skillset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyID', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('contact_details', models.CharField(default='', max_length=100)),
                ('accepting_interns', models.BooleanField(default=False)),
                ('openings_job_description', models.TextField(blank=True)),
                ('required_skills', models.ManyToManyField(to='Lexicon_App.skillset')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('username', models.CharField(default='', max_length=150, unique=True)),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('student_ID', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('password', models.CharField(default='', max_length=100)),
                ('confirm_password', models.CharField(default='', max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('social_security_number', models.CharField(max_length=20)),
                ('postal_address', models.CharField(max_length=200)),
                ('knowledge_level', models.CharField(max_length=100)),
                ('GDPR_consent', models.BooleanField(default=False)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv/')),
                ('linkedin_ID', models.URLField(blank=True, null=True)),
                ('github_ID', models.URLField(blank=True, null=True)),
                ('course', models.ManyToManyField(related_name='students', to='Lexicon_App.course')),
                ('skills', models.ManyToManyField(to='Lexicon_App.skillset')),
            ],
        ),
    ]
