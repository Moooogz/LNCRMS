# Generated by Django 4.2.5 on 2023-11-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_patienthistory_objectives_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patienthistory',
            name='bodytemp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='height',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='weight',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
