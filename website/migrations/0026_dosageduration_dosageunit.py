# Generated by Django 4.2.5 on 2023-12-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_alter_prescription_dosage_alter_prescription_evening_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dosageduration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage_duration', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dosageunit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage_unit', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]