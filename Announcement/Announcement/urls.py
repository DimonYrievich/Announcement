
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('GDY/', admin.site.urls),                              # admin
    path('pages/', include('django.contrib.flatpages.urls')),   # чтобы добавились ссылки на наши странички
    path('ckeditor/', include('ckeditor_uploader.urls')),       # !!!Нужны настройки!!! См. документацию !!!Возможно должно быть - path('ckeditor/', include('ckeditor.urls'))
    path('board/', include('Board.urls')),                      # чтобы все адреса из нашего приложения (Board/urls.py) подключались к главному приложению с префиксом board/
    path('sign/', include('sign.urls')),                        # все страницы, URL которых начинается с sign/, перенаправляем в приложение sign
    path('accounts/', include('allauth.urls')),
]
