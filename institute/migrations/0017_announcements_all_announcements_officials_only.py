# Generated by Django 4.0.4 on 2022-06-25 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0016_alter_student_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcements',
            name='all',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='announcements',
            name='officials_only',
            field=models.BooleanField(default=False),
        ),
    ]
