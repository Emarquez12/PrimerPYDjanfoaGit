from django.db import models
from elements.models import Element

# Create your models here.

class Comment(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    element = models.ForeignKey(Element, on_delete=models.CASCADE, null=True, blank=True)
    
    def formatted_datePost(self):
        return self.date_posted.strftime('%Y-%m-%d %I:%M %p')
    
    def __str__(self):
        return 'Comment #{}'.format(self.id)
    
    
    
