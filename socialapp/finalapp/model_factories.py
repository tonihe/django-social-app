import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File 
from .models import *
from faker import Faker
import random

fake = Faker()
user_name = fake.name()
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User 

    username = user_name.strip().replace(" ", "")
    email = user_name.strip().replace(" ", "")+"@gmail.com"
    password = "123456a!!!"
    id = random.randint(1000, 2000)

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    body = "Hello World!"
    author = factory.SubFactory(UserFactory)

class UserProfileFactory(factory.django.DjangoModelFactory):    
    user = factory.SubFactory(UserFactory)
    
    class Meta:
        model = UserProfile