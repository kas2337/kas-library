from rest_framework.serializers import ModelSerializer

from .models import Article, Note, Tag


class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ArticlesSerializer(ModelSerializer):
    tag = TagsSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = "__all__"


class NotesSerializer(ModelSerializer):
    tag = TagsSerializer(read_only=True, many=True)

    class Meta:
        model = Note
        fields = "__all__"
