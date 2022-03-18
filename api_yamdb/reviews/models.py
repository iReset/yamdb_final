from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER_ROLE = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]

    username = models.CharField('username', max_length=150, unique=True)
    email = models.EmailField('email', max_length=254, unique=True)
    first_name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    role = models.CharField('Роль', max_length=16,
                            choices=USER_ROLE, default=USER)
    bio = models.TextField('Биография', blank=True)

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_staff

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


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
    genre = models.ManyToManyField(
        Genre,
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
        # FIXME: а как без него???
        null=True,
        related_name='reviews',
        verbose_name='Произведение'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва'
    )
    text = models.TextField(
        'Текст отзыва',
        help_text='Введите отзыв на произведение'
    )
    score = models.IntegerField(
        'Оценка',
        help_text='Поставьте оценку',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    rev_pub_date = models.DateTimeField(
        'Дата отзыва',
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-rev_pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    text_comment = models.TextField(
        'Комментарий',
        help_text='Введите коментарий на отзыв',
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

    class Meta:
        ordering = ('-com_pub_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:15]
