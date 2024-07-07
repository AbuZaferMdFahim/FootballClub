# Generated by Django 5.0.6 on 2024-07-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_remove_fixture_name_fixture_match_fixture_opponent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kit', models.IntegerField(unique=True)),
                ('position', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('team', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('img', models.ImageField(upload_to='player_images/')),
            ],
        ),
    ]
