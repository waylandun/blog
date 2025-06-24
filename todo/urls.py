from django.urls import path

from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('toggle/<int:item_id>/', views.toggle_complete, name='todo_toggle'),
]
