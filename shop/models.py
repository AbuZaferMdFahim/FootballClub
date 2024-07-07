from django.db import models

# Create your models here.


class Jersey(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    img = models.ImageField(upload_to='jersey_images/')

    def __str__(self):
        return self.name
    
class FootballAccessory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='accessory_images/')

    def __str__(self):
        return self.name
    
class Turf(models.Model):
    model = models.CharField(max_length=100)
    description = models.TextField()
    price_per_square_meter = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    img = models.ImageField(upload_to='turf_images/')

    def __str__(self):
        return self.model
