# Generated by Django 5.0.6 on 2024-07-09 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_turf_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jersey',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
