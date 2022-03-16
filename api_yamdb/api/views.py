from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from reviews.models import Category, Comment, Genre, Review, Title, User

#from .serializers import


class UserViewSet(viewsets.ModelViewSet):
    pass

    queryset = User.objects.all()
    # serializer_class =
    # permission_classes = Admin

class CategoryViewSet(viewsets.ModelViewSet):
    pass

    queryset = Category.objects.all()
    # serializer_class =
    # permission_classes = Admin


class GenreViewSet(viewsets.ModelViewSet):
    pass

    queryset = Genre.objects.all()
    # serializer_class =
    # permission_classes = Admin

class CommentViewSet(viewsets.ModelViewSet):
    pass

    queryset = Comment.objects.all()
    # serializer_class =
    # permission_classes = Auth


class ReviewViewSet(viewsets.ModelViewSet):
    pass

    queryset = Review.objects.all()
    # serializer_class =
    # permission_classes = Auth


class TitleViewSet(viewsets.ModelViewSet):
    pass

    queryset = Title.objects.all()
    # serializer_class =
    # permission_classes = Admin
