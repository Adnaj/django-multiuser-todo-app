from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('todo-delete/<int:id>',views.tododelete,name='tododelete'),
    path('todo-update/<str:id>',views.todoupdate,name='update'),
    path('logout/',views.signout,name='logout')
    
]