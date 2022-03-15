from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    # Изменить setting -> AUTH_USER_MODEL = 'reviews.User'
    # username =
    # email =
    # role =
    # bio =
    # first_name =
    # last_name =


class Category(models.Model):
    pass

    name = models.CharField('категория', max_length=256)
    slug = models.SlugField('слаг категории', unique=True)

    def __str__(self):
        return f'{self.name} {self.slug}'


class Genre(models.Model):
    pass

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


class Review(models.Model):
    pass
    # title_id
    # text =
    # score =
    # author =
    # pub_date =


class Title(models.Model):
    pass

    name = models.CharField('титул', max_length=100)    
    year = models.IntegerField('год')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    description = models.TextField(
        'описание',
        max_length=256,
        null=True,
        blank=True,
        )

    def __str__(self):
        return f'{self.name}'
