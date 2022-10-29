from django.urls import path
from .views import ProjectCreateAPI, TaskCreateAPI, ProjectListAPI, TaskListProjectAPI, TaskListUserAPI


urlpatterns = [
      path('create', ProjectCreateAPI.as_view()),
      path('list', ProjectListAPI.as_view()),
      path('task/create', TaskCreateAPI.as_view()),
      path('task/list/<int:ProjectID>', TaskListProjectAPI.as_view()),
      path('task/list/user/<int:ProjectID>', TaskListUserAPI.as_view()),
]