import django_filters.rest_framework as filters
from reviews.models import Category, Genre, Title


class TitleFilter(filters.FilterSet):
    """Класс фильтра для модели произведение."""
    category = filters.ModelMultipleChoiceFilter(
        field_name='category__slug', to_field_name='slug',
        queryset=Category.objects.all())
    genre = filters.ModelMultipleChoiceFilter(
        field_name='genre__slug', to_field_name='slug',
        queryset=Genre.objects.all())
    name = filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Title
        fields = ('category', 'genre', 'name', 'year', )
