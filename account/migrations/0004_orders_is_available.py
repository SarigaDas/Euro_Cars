# Generated by Django 4.2.4 on 2023-09-12 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
