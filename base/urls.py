from django.urls import path
from . import views

app_name='base'

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('room/<int:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="createRoom"),
    path('update-room/<int:pk>/', views.updateRoom, name="updateRoom"),
    path('delete-room/<int:pk>/', views.deleteRoom, name="deleteRoom"),
]
