from django.urls import path
from tasks.views import taskList, taskView, yourName

urlpatterns = [
  path('', taskList, name='task-list'),
  path('task/<int:id>', taskView, name='task-view'),
  path('yourname/<str:name>', yourName, name='your-name'),
]