from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
from django.db import models


CHOICES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


class CustomUserManager(UserManager):
    pass


class User(AbstractUser):
    username = models.CharField('username', max_length=150, unique=True)
    email = models.EmailField('email', max_length=254, unique=True)
    first_name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    role = models.CharField('Роль', max_length=16, choices=CHOICES)
    bio = models.TextField('Биография', blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Category(models.Model):
    name = models.CharField('категория', max_length=256)
    slug = models.SlugField('слаг категории', unique=True)

    def __str__(self):
        return f'{self.name} {self.slug}'


class Genre(models.Model):
    name = models.CharField('жанр', max_length=100)
    slug = models.SlugField('слаг жанра', unique=True)

    def __str__(self):
        return f'{self.name} {self.slug}'


class Title(models.Model):
    name = models.CharField('титул', max_length=100)
    year = models.IntegerField('год')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
    )
    genre = models.ForeignKey(  # ManyToMany?
        Genre,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
    )
    description = models.TextField(
        'описание',
        max_length=256,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    text = models.TextField(
        'Отзыв',
        help_text='Введите отзыв на произведение'
    )
    score = models.IntegerField(
        'Оценка',
        help_text='Поставьте оценку',
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    rev_pub_date = models.DateTimeField(
        'Дата отзыва',
        auto_now_add=True,
    )


class Comment(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Произведение'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    text_comment = models.TextField(
        'Комментарий',
        help_text='Введите коментарий на отзыв'
    )
    com_pub_date = models.DateTimeField(
        'Дата комментария',
        auto_now_add=True,
    )
    constraints = [
        models.UniqueConstraint(
            fields=['title', 'review'],
            name='unique_review_for_title')
    ]
