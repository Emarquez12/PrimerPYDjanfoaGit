from django.test import TestCase
from faker import Faker
from .models import Comment

# Create your tests here.

def main():
    faker = Faker()
    
    for _ in range(5):
        comment = Comment.objects.create(
            text=faker.text(),
            date_posted=faker.date_time_this_year()
        )
        
        comment = Comment.objects.all()
        print(f'Comments in BD {comment.count()}')
     
main()