from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from lib.permissions import IsProjectManager
from task.serializers import ProjectSerializer, TaskSerializer, TaskListSerializer
from .models import Project, Task


class ProjectCreateAPI(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsProjectManager)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectListAPI(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskCreateAPI(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save()


class TaskListProjectAPI(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return Task.objects.filter(project=self.kwargs['ProjectID']).order_by('-id')


class TaskListUserAPI(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return Task.objects.filter(
            project=self.kwargs['ProjectID'],
            assignee=self.request.user).order_by('-id')
