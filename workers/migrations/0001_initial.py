# Generated by Django 3.0.6 on 2020-09-23 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institute', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_email', models.EmailField(max_length=254, unique=True)),
                ('staff_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(choices=[('Scavenger', 'Scavenger'), ('General Servant', 'General Servant'), ('Doctor', 'Doctor'), ('Mess Incharge', 'Mess Incharge'), ('Electrician', 'Electrician'), ('Gym Trainer', 'Gym Trainer'), ('PT/Games Coach', 'PT/Games Coach')], max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institute.Block')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present_dates', models.TextField(blank=True, null=True)),
                ('absent_dates', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('worker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='workers.Worker')),
            ],
        ),
    ]
