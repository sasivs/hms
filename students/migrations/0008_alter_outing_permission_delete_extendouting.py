# Generated by Django 4.0.4 on 2022-06-13 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alter_outing_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outing',
            name='permission',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Granted', 'Granted'), ('Rejected', 'Rejected'), ('Revoked', 'Revoked'), ('Pending Extension', 'Pending Extension'), ('Processing Extension', 'Processing Extension'), ('Extension Granted', 'Extension Granted'), ('Extension Rejected', 'Extension Rejected')], default='Pending', max_length=20),
        ),
        migrations.DeleteModel(
            name='ExtendOuting',
        ),
    ]