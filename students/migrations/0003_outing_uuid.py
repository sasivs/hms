# Generated by Django 4.0.4 on 2022-06-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_outing_permission_alter_outing_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='outing',
            name='uuid',
            field=models.UUIDField(null=True, unique=True),
        ),
    ]