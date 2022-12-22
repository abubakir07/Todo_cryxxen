from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import RegisterView, TaskListView, TaskDetailView, DeleteAllTasksView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_refresh'),

    path('register/', RegisterView.as_view(), name='register'),
    path('task/list', TaskListView.as_view(), name='tasklist'),
    path('task/detail', TaskDetailView.as_view(), name='taskdetail'),
    path('task/all/delete', DeleteAllTasksView.as_view(), name='taskdelete')


    # path('login/', LoginView.as_view(), name='login')
]