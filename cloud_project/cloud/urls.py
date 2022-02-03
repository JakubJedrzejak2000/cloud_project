from django.urls import path

from . import views

urlpatterns = [

    path("", views.get_name, name="index"),
    path("delete", views.delete, name="delete"),

]