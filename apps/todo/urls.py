from django.urls import path

from .views import TodoCreateAPIView, TodoListAPIView, TodoDetailAPIView, TodoDeleteAllAPIView


urlpatterns = [
    path('create', TodoCreateAPIView.as_view(), name='todo_create'),
    path('list', TodoListAPIView.as_view(), name='todo_list'),
    path('list/<int:pk>', TodoDetailAPIView.as_view(), name='todo_detail'),
    path('all/delete', TodoDeleteAllAPIView.as_view(), name='todo_all_delete')
]