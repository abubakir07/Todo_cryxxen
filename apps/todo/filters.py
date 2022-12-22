import django_filters
from .models import Todo

class TodoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateTimeFilter(lookup_expr='date__gte')
    is_completed = django_filters.BooleanFilter()

    class Meta:
        model = Todo
        fields = ['title', 'created_at', 'is_completed']