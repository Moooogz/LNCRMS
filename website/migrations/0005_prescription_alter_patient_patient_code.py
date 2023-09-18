# Generated by Django 4.2.5 on 2023-09-18 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_patient_patient_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('patient_code', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('medicine_name', models.CharField(max_length=100)),
                ('dosage', models.CharField(max_length=50)),
                ('morning', models.CharField(max_length=50)),
                ('noon', models.CharField(max_length=50)),
                ('evening', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_code',
            field=models.CharField(max_length=50),
        ),
    ]
