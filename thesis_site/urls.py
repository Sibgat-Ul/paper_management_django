from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('thesis_topics/', views.thesis_topics, name='thesis_topics'),
    path('thesis_details/<int:id>/details', views.thesis_details, name='thesis_details'),
]