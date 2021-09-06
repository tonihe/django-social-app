import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from .serializer import *

class Social_API_Endpoint_Test(APITestCase):

    good_url = None 
    bad_url = None 


    def setUp(self):
        self.good_url = reverse('post-detail-api', kwargs={"pk": 76})
        self.bad_url = reverse('post-detail-api', kwargs={"pk": 1})
        self.profile = reverse('profile-api')
        self.post_list = reverse('post-api')
    
    def test_post_factory_pass(self):
        print(self.good_url)
        response = self.client.get(self.good_url, format='json')
        response.render()
        print(response)
        self.assertEquals(response.status_code, 404)
    
    def test_post_factory_fail(self):
        print(self.bad_url)
        response = self.client.get(self.bad_url, format='json')
        response.render()
        print(response)
        self.assertEquals(response.status_code, 404)
    
    def test_profile_api(self):
        print(self.profile)
        response = self.client.get(self.profile, format='json')
        response.render()
        print(response)
        self.assertEquals(response.status_code, 200)

    def test_post_list_api(self):
        print(self.post_list)
        response = self.client.get(self.post_list, format='json')
        response.render()
        print(response)
        self.assertEquals(response.status_code, 200)

