# Generated by Django 4.2.5 on 2023-12-11 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_dosageduration_dosageunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='medicine_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='patient_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='quantity',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
