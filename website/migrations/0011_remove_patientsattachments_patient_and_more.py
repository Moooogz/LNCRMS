# Generated by Django 4.2.5 on 2023-09-24 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_remove_patientsattachments_patient_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientsattachments',
            name='patient',
        ),
        migrations.AddField(
            model_name='patientsattachments',
            name='patient_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]