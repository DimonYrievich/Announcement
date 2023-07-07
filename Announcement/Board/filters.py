# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем, должен чем-то напомнить знакомые вам Django дженерики.
# В fields содержится словарь настройки самих фильтров. Ключами являются названия полей модели, а значениями выступают списки
# операторов фильтрации. Именно те, которые мы можем указать при составлении запроса.
# Например, Post.objects.filter(price__gt=10)
# Список операторов можно посмотреть по ссылке:	https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups
# По настройке внешнего вида фильтров и способа фильтрации см.  ниже с применением ModelChoiceFilter

from django_filters import FilterSet, ModelChoiceFilter
from .models import *
import django.forms

class PostFilter(FilterSet):
    class Meta:
        model = Post    # В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        # В fields мы описываем по каким полям модели будет производиться фильтрация.
        # Ключами являются названия полей модели, а значениями выступают списки операторов фильтрации.
        fields = {
            'category': ['exact'],
            'author': ['exact'],
        }

# ModelChoiceFilter - это выбор модели фильтра (как он будет выглядеть)
    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='----------------'
    )
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='------------------'
    )

class MypostsFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'category': ['exact'],
            # 'comment': [''],   !!!!Добавить в модели поста(Post) поле comment(коментарий)!!!!!
        }

    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='----------------'
    )