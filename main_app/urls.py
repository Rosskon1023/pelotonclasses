from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('classes/', views.classes_index, name='index'),
    path('classes/<int:class_id>/', views.classes_detail, name='detail'),
    path('classes/create/', views.ClassCreate.as_view(), name='classes_create'),
    path('classes/<int:pk>/delete/', views.ClassDelete.as_view(), name='classes_delete'),
    path('classes/<int:pk>/update/', views.ClassUpdate.as_view(), name='classes_update'),
    path('classes/<int:class_id>/add_artist/', views.add_artist, name='add_artist'),
]