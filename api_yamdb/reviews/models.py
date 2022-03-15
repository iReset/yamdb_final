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
    # name =
    # slug =


class Comment(models.Model):
    pass
    # review_id, title_id, comment_id
    # text =
    # author =
    # pub_date =


class Genre(models.Model):
    pass
    # name =
    # slug =


class Review(models.Model):
    pass
    # title_id
    # text =
    # score =
    # author =
    # pub_date =


class Title(models.Model):
    pass
    # name =
    # year =
    # category =
    # genre = ?
