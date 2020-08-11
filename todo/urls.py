from django.urls import path
from .views import TaskList, UpdateTask, CreateTask, DeleteTask


app_name = 'todo'
urlpatterns = [
    path('', TaskList.as_view(), name='index'),
    path('create', CreateTask.as_view(), name='create'),
    path('<int:pk>', UpdateTask.as_view(), name='update'),
    path('delete/<int:pk>', DeleteTask.as_view(), name='delete'),
]
