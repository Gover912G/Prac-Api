from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPostListCreate.as_view(), name='blogpost')
]