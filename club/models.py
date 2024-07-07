from django.db import models
from datetime import time

# Create your models here.


class Fixture(models.Model):
    opponent = models.CharField(max_length=100,default = None)
    date = models.DateTimeField(default = None)
    location = models.CharField(max_length=200,default = None)
    type = models.CharField(max_length = 100,default = None)
    match = models.CharField(max_length = 200,default = None)

    def __str__(self):
        return self.opponent
    

class Player(models.Model):
    GOALKEEPER = 'goalkeeper'
    DEFENDER = 'defender'
    MIDFIELDER = 'midfielder'
    STRIKER = 'striker'

    POSITION_CHOICES = [
        (GOALKEEPER, 'Goalkeeper'),
        (DEFENDER, 'Defender'),
        (MIDFIELDER, 'Midfielder'),
        (STRIKER, 'Striker'),
    ]
    name = models.CharField(max_length=100)
    kit = models.IntegerField(unique=True)
    position = models.CharField(
        max_length=50,
        choices=POSITION_CHOICES,
        default=MIDFIELDER,
    )
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    dob = models.DateField()
    img = models.ImageField(upload_to='player_images/')

    def __str__(self):
        return self.name
    

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



