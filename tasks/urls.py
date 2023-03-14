from django.urls import path
from tasks.views import taskList, taskView, newTask, yourName

urlpatterns = [
  path('', taskList, name='task-list'),
  path('task/<int:id>', taskView, name='task-view'),
  path('newtask/', newTask, name='new-task'),
  path('yourname/<str:name>', yourName, name='your-name'),
]