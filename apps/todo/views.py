from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import permissions, status


from .serializers import  TodoSerializer
from .models import Todo
from .permissions import IsOwner
from .filters import TodoFilter

class TodoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TodoFilter



class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsOwner]

    def get_object(self):
        obj = get_object_or_404(Todo, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj


class TodoDeleteAllAPIView(generics.DestroyAPIView):
    permission_classes = [IsOwner]

    def delete(self, request, *args, **kwargs):
        user = request.user
        tasks = Todo.objects.filter(user=user)
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


                
    


