from django.contrib import admin
from django.urls import path
from getdataapp import views
urlpatterns = [
    path('data/', views.get_data),
]
