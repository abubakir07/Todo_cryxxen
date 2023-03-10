from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('apps.todo.urls')),
    path('user/', include('apps.user.urls')),  
    path('swagger/', schema_view)
]



