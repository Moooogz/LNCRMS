# Generated by Django 4.2.5 on 2023-12-06 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_prescription_consultcounter'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='medduration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='medgenname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='medsize',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='medunit',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='qty',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
