# Generated by Django 4.2.5 on 2024-01-22 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0038_systemlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemlog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
