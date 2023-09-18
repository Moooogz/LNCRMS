# Generated by Django 4.2.5 on 2023-09-18 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_prescription_alter_patient_patient_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patienthistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('consultCounter', models.DateTimeField(auto_now_add=True)),
                ('patient_code', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='remarks',
        ),
    ]
