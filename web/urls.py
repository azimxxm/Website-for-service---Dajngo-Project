from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article', views.article, name='article'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
]

