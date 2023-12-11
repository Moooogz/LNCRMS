# Generated by Django 4.2.5 on 2023-12-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_alter_prescription_medicine_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='medunit',
            new_name='durationqty',
        ),
        migrations.RenameField(
            model_name='prescription',
            old_name='medicine_name',
            new_name='medname',
        ),
        migrations.RenameField(
            model_name='prescription',
            old_name='qty',
            new_name='medqty',
        ),
        migrations.RenameField(
            model_name='prescription',
            old_name='quantity',
            new_name='medtype',
        ),
        migrations.AddField(
            model_name='prescription',
            name='perduration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='totalquantity',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
