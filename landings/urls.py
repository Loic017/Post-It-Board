from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('faq/', views.faq, name="faq"),
    path('pricing/', views.pricing, name="pricing"),
]
