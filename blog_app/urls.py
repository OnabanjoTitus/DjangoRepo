from django.urls import path

from .views import Blog_App_Views

urlpatterns = [
    path('', Blog_App_Views(), name='home')
]
