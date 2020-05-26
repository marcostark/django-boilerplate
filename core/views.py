from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework import generics, permissions
from . import serializers
from . import models


class TaskListView(generics.ListAPIView):

    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    ordering_fields = '__all__'
    filter_fields = '__all__'
    search_fields = 'nome'
    # Descomentar para utilizar os filtros e a autenticação
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # permission_classes = (permissions.IsAuthenticated,)