from django.db import models

# Create your models here.
class MenuItems(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    inventory = models.SmallIntegerField()
    
    def __self__(self):
        return self.title
