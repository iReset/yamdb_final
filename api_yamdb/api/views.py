# from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# from .permissions import AdminOrReadOnly
from reviews.models import Category, Comment, Genre, Review, Title, User

from .filters import TitleFilter
from .mixins import CreateListDestroyViewSet
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, GetTitleSerializer,
                          ReviewSerializer, TitleSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)


class CategoryViewSet(CreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    # permission_classes = (AdminOrReadOnly,)


class GenreViewSet(CreateListDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    # permission_classes = (AdminOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = Auth


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = Auth


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    )
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    # permission_classes = (AdminOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetTitleSerializer
        return TitleSerializer
