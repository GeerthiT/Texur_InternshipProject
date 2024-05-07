# Generated by Django 4.2.7 on 2024-05-07 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Lexicon_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='testStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameField(
            model_name='company',
            old_name='openings_job_description',
            new_name='openings_internship_description',
        ),
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(default='Unknown', max_length=255),
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
            name='phone',
            field=models.CharField(default='Unknown', max_length=15),
        ),
        migrations.AddField(
            model_name='company',
            name='size',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.URLField(default='http://example.com'),
        ),
        migrations.AddField(
            model_name='course',
            name='skills',
            field=models.ManyToManyField(to='Lexicon_App.skillset'),
        ),
        migrations.AddField(
            model_name='student',
            name='has_internship',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='postal_address',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.CreateModel(
            name='InternshipPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lexicon_App.company')),
            ],
        ),
    ]