from django.urls import path
from aplication import views

urlpatterns = [
    path("", views.index, name="index"),
    path('rooms/', views.room_list, name='room_list'),
    path('workers/', views.worker_list, name='worker_list'),
    path('roomdelail/<int:pk>/', views.room_detail, name='room_detail')
    ]