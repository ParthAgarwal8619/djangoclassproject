from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('update/<int:id>',views.update_member, name="update_member"),
    path('delete/<int:id>',views.delete_member, name="delete_member"),
]