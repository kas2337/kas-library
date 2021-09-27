from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import Article, Note, Tag
from .serializers import ArticlesSerializer, NotesSerializer, TagsSerializer


class ArticlesViews(ModelViewSet):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class NotesViews(ModelViewSet):
    model = Note
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class TagsViews(ModelViewSet):
    model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
