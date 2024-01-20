from django.contrib import admin
from django.urls import path
from . import views

app_name = "todos"
 
urlpatterns = [
    path('', views.index),
    path("todos/create",views.createTodo),
    path("todos/update/<int:id>", views.updateTodo),
    # path("todos/delete/<int:id>", views.deleteTodo, name="todo.delete"),
    ]








