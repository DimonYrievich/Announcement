from django import forms
from .models import *
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    #author = forms.ModelChoiceField(queryset=Author.objects.all(), label='Автор', empty_label='------------------')
    #category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='----------------')
    class Meta:
        model = Post
        fields = [               # fields = '__all__'    # - можно и так, но тогда Django будет брать все поля из модели
            'title',
            'text',
            'content',
            'author',
            'category',
        ]

        # # Можно немного поменять визуальное представление формы заполнения поста (объявления).
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'my-custom-class', 'placeholder': 'Напиши заголовок'}),
        #     'text': forms.Textarea(attrs={'class': 'my-custom-class', 'rows': 3, 'placeholder': 'Напиши текст'}),
        #     'content': forms.Textarea(attrs={'class': 'my-custom-class', 'rows': 5}),
        #     'author': forms.Select(attrs={'class': 'my-custom-class'}),
        #     'category': forms.Select(attrs={'class': 'my-custom-class'}),
        # }

# Валидация формы
    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get("title")
        if title is not None and len(title) < 1:
            raise ValidationError({"title": "Заголовок не может быть менее 1 символа."})

        text = cleaned_data.get("text")
        if text is not None and len(text) < 10:
            raise ValidationError({"text": "Текст обэявления не может быть менее 10 символов."})

        author = cleaned_data.get("author")
        if not author:
            raise ValidationError({"author": "Обязательно укажите автора."})

        category = cleaned_data.get("category")
        if not category:
            raise ValidationError({"category": "Обязательно укажите категорию объявления."})

        return cleaned_data