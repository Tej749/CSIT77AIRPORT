from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("", views.table, name="table"),
    path("form", views.form, name="form"),
    path("form/edit/<pk>", views.edit, name="edit"),
    path("contact", views.contact, name="contact"),

]