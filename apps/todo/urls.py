from django.urls import path

from .views import  TodoListCreateAPIView, TodoDetailAPIView, TodoDeleteAllAPIView


urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view(), name='todo_list'),
    path('todos/<int:pk>/', TodoDetailAPIView.as_view(), name='todo_detail'),
    path('all/delete/', TodoDeleteAllAPIView.as_view(), name='todo_all_delete')
]