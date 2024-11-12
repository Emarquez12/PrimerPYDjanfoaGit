from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError

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
    slug  = models.SlugField(max_length=250,blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def adminCreateDate(self):
        return self.create.strftime('%Y-%m-%d %I:%M %p')
    adminCreateDate.short_description = 'Fecha de Creación'
    
    def adminUpdateDate(self):
        return self.update.strftime('%Y-%m-%d %I:%M %p')
    adminUpdateDate.short_description = 'Última Actualización'
    
    @admin.display(boolean=True)
    def cheap(self):
        return 0 <= self.price < 9.99
    
    def _str_(self):
        return self.title
    
    def clean(self):
        if self.price < 0:
            raise ValidationError("Precio no puede ser negativo.")