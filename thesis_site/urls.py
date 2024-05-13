from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add_thesis/', views.add_thesis, name='add_thesis'),
    path('thesis_topics/', views.thesis_topics, name='thesis_topics'),

    path('thesis_details/<int:id>/details', views.thesis_details, name='thesis_details'),
    path('thesis_details/<int:id>/edit', views.edit_thesis, name='thesis_edit'),
    path('thesis_details/<int:id>/delete', views.delete_thesis, name='thesis_delete'),
]