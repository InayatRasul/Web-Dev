from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    category = models.CharField(max_length=200)

    def to_json(self):
        return{
            'name':self.name,
            'price':self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active,
            'category': self.category
        }

class Category(models.Model):
    name = models.CharField(max_length=200)

    def to_json(self):
        return {
            'name': self.name
        }
    def get_name(self):
        return self.name
