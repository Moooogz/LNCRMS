# Generated by Django 4.2.5 on 2023-09-13 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_patient_bday_patient_civil_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicinelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('medicine_name', models.CharField(max_length=100)),
                ('dosage', models.CharField(max_length=50)),
            ],
        ),
    ]