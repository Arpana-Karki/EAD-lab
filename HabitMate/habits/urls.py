from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.habit_list, name='habit_list'),
    path('add/', views.add_habit, name='add_habit'),
    path('edit/<int:pk>/', views.edit_habit, name='edit_habit'),
    path('delete/<int:pk>/', views.delete_habit, name='delete_habit'),
    path('toggle/<int:pk>/', views.toggle_habit, name='toggle_habit'),
]
