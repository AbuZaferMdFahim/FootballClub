# Generated by Django 5.0.6 on 2024-07-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('goalkeeper', 'Goalkeeper'), ('defender', 'Defender'), ('midfielder', 'Midfielder'), ('striker', 'Striker')], default='midfielder', max_length=50),
        ),
    ]
