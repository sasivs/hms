# Generated by Django 4.0.4 on 2022-06-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0019_alter_vacation_vacated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outing',
            name='type',
            field=models.CharField(choices=[('Local', 'Local'), ('Non-Local', 'Non-Local'), ('Emergency', 'Emergency'), ('Vacation', 'Vacation')], max_length=9),
        ),
    ]