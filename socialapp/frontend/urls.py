from django.urls import path
from frontend.views import index

urlpatterns = [
    path('', index.as_view(), name='index'),
]