# Generated by Django 4.2.5 on 2023-10-04 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_alter_patienthistory_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsattachments',
            name='consultCounter',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
