
from django.contrib import admin
from .models import Category, Post, Author, PostCategory

#Регистрируем все созданные модели для отображения их в админке
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(PostCategory)