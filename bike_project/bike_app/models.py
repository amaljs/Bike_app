from django.db import models

# Create your models here.
class New_bikes(models.Model):
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    price=models.CharField(max_length=100)

    def __str__(self):
        return self.name