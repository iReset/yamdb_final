from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Изменить setting -> AUTH_USER_MODEL = 'reviews.User'
    # username =
    # email =
    # role =
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    # first_name =
    # last_name =


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


class Comment(models.Model):
    pass
    # review_id, title_id, comment_id
    # text =
    # author =
    # pub_date =


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
        User,
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
