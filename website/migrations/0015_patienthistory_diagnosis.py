# Generated by Django 4.2.5 on 2023-09-24 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_patientsattachments_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='patienthistory',
            name='diagnosis',
            field=models.CharField(blank=True, default='*under observation', max_length=500, null=True),
        ),
    ]
