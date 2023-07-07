
from django.db import models
from django.core.validators import MinValueValidator
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse

########################################################################################################################

class Author(models.Model):
    name_author = models.OneToOneField(User, on_delete=models.CASCADE)  #cвязь «один к одному» с встроенной моделью User
    objects = None
    def __str__(self):
        return self.name_author.username

########################################################################################################################

class Category(models.Model):
    tanks = 'Танки'
    hills = 'Хилы'
    dd = 'ДД'
    tradesmen = 'Торговцы'
    guildmasters = 'Гилдмастеры'
    questgivers = 'Квестгиверы'
    blacksmiths = 'Кузнецы'
    tanners = 'Кожевники'
    potionmakers = 'Зельевары'
    spellmasters = 'Мастера заклинаний'

    POSITIONS = [
        (tanks, 'Танки'),
        (hills, 'Хилы'),
        (dd, 'ДД'),
        (tradesmen, 'Торговцы'),
        (guildmasters, 'Гилдмастеры'),
        (questgivers, 'Квестгиверы'),
        (blacksmiths, 'Кузнецы'),
        (tanners, 'Кожевники'),
        (potionmakers, 'Зельевары'),
        (spellmasters, 'Мастера заклинаний'),
    ]
    objects = None
    name_category = models.CharField(max_length=20, choices = POSITIONS, default = tanks, unique = True)
#    subscribers = models.ManyToManyField(User, related_name='category')   #Поле subscribers (соотношение manytomany), в которое будут записываться пользователи, подписанные на обновления в данной категории.

    def __str__(self):
        return self.name_category

#########################################################################################################################

class Post(models.Model):
    objects = None
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    content = RichTextField()     # Поле текста так называемое WYSIWYG-поле (поле «текст, внутри которого могут быть картинки, встроенные видео и другой контент»)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)             #связь «один ко многим» с моделью Author
    category = models.ManyToManyField('Category', through = 'PostCategory', related_name='post')

    # Для вывода в HTML странице указываем, как должен выглядеть объект нашей модели (что именно нужно выводить)
    def __str__(self):
        return f'{self.title} {self.text[:1000]} {self.time_in} {self.author} {self.category} {self.content}'

    # Добавим метод get_absolute_url, чтобы указать, какую страницу нужно открыть после создания поста
    # Функция reverse позволяет указать не путь вида /board/…, а название пути.
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

#######################################################################################################################
                                            #Промежуточная таблица
class PostCategory(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post}:{self.category}'

#######################################################################################################################