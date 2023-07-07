from django.urls import reverse_lazy
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import *
from .filters import PostFilter, MypostsFilter
from .forms import PostForm
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404
# from django.shortcuts import redirect
# from django.contrib.auth.models import Group
# from django.core.cache import cache                     # импортируем кэш
# from django.http import HttpResponse                    # импортируем для перевода, проверки текстов
# from django.views import View
# from django.utils import timezone                       # для локализации времени
# import pytz


class PostsList(ListView):               # ПРЕДСТАВЛЕНИЕ. Создаем свой класс, который наследуется от ListView (для отображения СПИСКА всех объявлений)
    model = Post                         # Указываем модель, объекты которой мы будем выводить
    post_title = 'title'                 # Поле, которое будет использоваться для сортировки объектов (необязательно)
    template_name = 'posts_list.html'    # Указываем имя шаблона, в котором будут все инструкции о том, как именно пользователю должны быть показаны наши объекты
    context_object_name = 'posts'        # Имя списка, в котором будут лежать все объекты. Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    paginate_by = 4                      # ПАГИНАЦИЯ. Так мы можем указать количество записей на web-странице + нужно внести изменения в шаблоне HTML

    # Фильтрация
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs.order_by('-time_in')
    # Фильтрация
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class MypostsList(LoginRequiredMixin, ListView):          # ПРЕДСТАВЛЕНИЕ. Для отображения СПИСКА всех своих объявлений
    model = Post
    template_name = 'my_list.html'
    context_object_name = 'myposts'     # Имя списка, в котором будут лежать все объекты. Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    paginate_by = 4

    # Фильтрация
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MypostsFilter(self.request.GET, queryset=queryset)
        #return Post.objects.filter(author__name_author=self.request.user).order_by('-time_in') - так было до добавления фильтрации
        return self.filterset.qs.filter(author__name_author=self.request.user).order_by('-time_in')
    # Фильтрация
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):          #ПРЕДСТАВЛЕНИЕ Создаем свой класс, который наследуется от DetailView для отображения одного экземпляра таблицы из БД.
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class TanksList(ListView):
    model = Post
    template_name = 'tanks.html'
    context_object_name = 'tanks'

    def get_queryset(self):
        return Post.objects.filter(category__name_category='Танки')

class HillsList(ListView):
    model = Post
    template_name = 'hills.html'
    context_object_name = 'hills'

    def get_queryset(self):
        return Post.objects.filter(category__name_category='Хилы')

class DDList(ListView):
    model = Post
    template_name = 'dd.html'
    context_object_name = 'dd'

    def get_queryset(self):
        return Post.objects.filter(category__name_category='ДД')

class TradesmenList(ListView):
    model = Post
    template_name = 'tradesmen.html'
    context_object_name = 'tradesmen'

    def get_queryset(self):
        return Post.objects.filter(category__name_category='Торговцы')

class GuildmastersList(ListView):
    model = Post
    template_name = 'guildmasters.html'
    context_object_name = 'guildmasters'

    def get_queryset(self):
        return Post.objects.filter(category__name_category='Гилдмастеры')

class QuestgiversList(ListView):
    model = Post
    template_name = 'questgivers.html'
    context_object_name = 'questgivers'

    def get_queryset(self):
        return Post.objects.filter(category__name_category='Квестгиверы')

class BlacksmithsList(ListView):
    model = Post
    template_name = 'blacksmiths.html'
    context_object_name = 'blacksmiths'

    def get_queryset(self):
        return Post.objects.filter(category__name_category='Кузнецы')

class TannersList(ListView):
    model = Post
    template_name = 'tanners.html'
    context_object_name = 'tanners'

    def get_queryset(self):
        return Post.objects.filter(category__name_category='Кожевники')

class PotionmakersList(ListView):
    model = Post
    template_name = 'potionmakers.html'
    context_object_name = 'potionmakers'

    def get_queryset(self):
        return Post.objects.filter(category__name_category='Зельевары')

class SpellmastersList(ListView):
    model = Post
    template_name = 'spellmasters.html'
    context_object_name = 'spellmasters'

    def get_queryset(self):
        return Post.objects.filter(category__name_category='Мастера заклинаний')

class PostCreate(CreateView, PermissionRequiredMixin):   #ПРЕДСТАВЛЕНИЕ для создания публикации
    form_class = PostForm                                # Указываем нашу разработанную форму
    model = Post                                         # Указываем модель
    template_name = 'post_create.html'                   # Указываем шаблон, в котором используется форма

#     permission_required = ('news.add_post',
#                            'news.delete_post',
#                            'news.view_post',
#                            'news.change_post',)          #добавил, но под??? см.ниже ПРЕДСТАВЛЕНИЕ: Ограничения и права доступа пользователя
#     success_url = reverse_lazy('post_list')              #добавил
#
# #    def form_valid(self, form):
# #        post = form.save(commit=False)
# #        post.choice_field = 'news'      # либо 'post' либо 'posts' ?????????????????????????
# #        post.author = Author.objects.get(user=self.request.user)
# #        return super().form_valid(form)
#
#
class PostUpdate(UpdateView, LoginRequiredMixin):     #ПРЕДСТАВЛЕНИЕ для изменения публикации.
    form_class = PostForm                             #Будем использовать ту же форму, что и для создания публикации
    model = Post
    template_name = 'post_create.html'                #Будем использовать тот же шаблон, что и для создания публикации
    success_url = reverse_lazy('myposts')             # Указываем, куда перенаправить пользователя после изменения поста

class PostDelete(DeleteView):                         #ПРЕДСТАВЛЕНИЕ удаляющее публикацию.
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('myposts')             # Указываем, куда перенаправить пользователя после удаления поста

class IndexView(LoginRequiredMixin, TemplateView):      #*
    template_name = 'index.html'                        #*