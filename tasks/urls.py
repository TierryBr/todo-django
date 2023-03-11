from django.urls import path
from tasks.views import taskList, yourName

urlpatterns = [
  path('', taskList, name='task-list'),
  path('yourname/<str:name>', yourName, name='your-name'),
]