from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250)
    slug  = models.SlugField(max_length=250)
    
    def __str__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=250)
    slug  = models.SlugField(max_length=250)
    
    def __str__(self):
        return self.title

class Element(models.Model):
    title = models.CharField(max_length=250)
    slug  = models.SlugField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def _str_(self):
        return self.title