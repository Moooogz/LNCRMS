# Generated by Django 4.2.5 on 2023-12-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_dosageduration_daysqty_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicinelist',
            name='medgenname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='medicinelist',
            name='medname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='medicinelist',
            name='medsize',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]