from rest_framework import viewsets
from .serializers import TaskSerializers, TagSerializers
from webapp.models import Task, Tag


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
