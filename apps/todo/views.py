from django_filters import rest_framework as filters
# from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status, filters

from .serializers import  TodoSerializer
from .models import Todo
from .permissions import IsOwner
from .filters import TodoFilter


class TodoCreateAPIView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes=[IsAuthenticated]
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class TodoListAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ['title', 'created_at', 'is_completed']
    ordering_fields = ['is_completed', 'created_at']
    search_fields = ['title', 'created_at']
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)



class TodoDeleteAllAPIView(generics.DestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsOwner]

    def delete(self, request, *args, **kwargs):
        user = request.user
        tasks = Todo.objects.filter(user=user)
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

                
    


