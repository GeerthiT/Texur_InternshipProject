# Generated by Django 5.0.3 on 2024-05-12 22:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lexicon_App', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='accepting_interns',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='company',
            name='contact_details',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='contact_person_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='contact_person_position',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(default='info@example.com', max_length=254, verbose_name='User Email'),
        ),
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='openings_internship_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(default='Unknown', max_length=15),
        ),
        migrations.AddField(
            model_name='company',
            name='required_skills',
            field=models.ManyToManyField(to='Lexicon_App.skillset'),
        ),
        migrations.AddField(
            model_name='company',
            name='size',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='company_profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.URLField(default='http://example.com'),
        ),
    ]