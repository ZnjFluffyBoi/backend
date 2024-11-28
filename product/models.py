from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to="product/",null=True,blank=True)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.image} - {self.name} - {self.price} - {self.description} '
