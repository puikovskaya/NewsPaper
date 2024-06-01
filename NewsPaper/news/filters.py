from django.forms import DateInput
from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .models import Post, Author


class PostFilter(FilterSet):
    created_at = DateFilter(widget=DateInput(attrs={'type': 'date'}), lookup_expr='gt',
                            field_name='created_at', label='Дата публикации позднее')

    title = CharFilter(lookup_expr='icontains', field_name='title', label='Заголовок')
    author = ModelChoiceFilter(field_name='author', label='Имя автора', empty_label='Все авторы',
                               queryset=Author.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'author', 'created_at']
