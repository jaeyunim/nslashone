from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainHome, name="mainHome"),
]
