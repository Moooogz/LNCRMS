# Generated by Django 4.2.5 on 2023-09-18 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_patienthistory_remove_patient_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienthistory',
            name='consultCounter',
            field=models.CharField(max_length=50),
        ),
    ]
