
from django.urls import path
from .views import *				# Импортируем все созданные нами представления

urlpatterns = [
	path('', PostsList.as_view(), name='posts'),						# name='_____' - название пути
	path('', IndexView.as_view()),										#*
	path('<int:pk>', PostDetail.as_view(), name='post_detail'),
	path('I/', MypostsList.as_view(), name='myposts'),
	path('tanks/', TanksList.as_view(), name='tanks'),
	path('hills/', HillsList.as_view(), name='hills'),
	path('dd/', DDList.as_view(), name='dd'),
	path('tradesmen/', TradesmenList.as_view(), name='tradesmen'),
	path('guildmasters/', GuildmastersList.as_view(), name='guildmasters'),
	path('questgivers/', QuestgiversList.as_view(), name='questgivers'),
	path('blacksmiths/', BlacksmithsList.as_view(), name='blacksmiths'),
	path('tanners/', TannersList.as_view(), name='tanners'),
	path('potionmakers/', PotionmakersList.as_view(), name='potionmakers'),
	path('spellmasters/', SpellmastersList.as_view(), name='spellmasters'),
	path('create/', PostCreate.as_view(), name='post_create'),
	path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
	path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]