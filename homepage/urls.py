from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage_home, name="homepage_home")
]
