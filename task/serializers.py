from rest_framework import serializers
from django.contrib.auth.models import User
from account.serializers import UserSerializer
from .models import Task, Project


class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'user', 'title', 'description',)


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'project', 'assignee', 'title', 'description',)


class TaskListSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    assignee = UserSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'project', 'assignee', 'title', 'description',)
