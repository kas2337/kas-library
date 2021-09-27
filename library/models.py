from django.utils.translation import ugettext_lazy as _

from django.db import models

from core.models import DateMixin, UserMixin


class Tag(DateMixin):
    tag_name = models.CharField(verbose_name=_("Тэг"), max_length=256, blank=True)


class BaseArticle(DateMixin, UserMixin):
    header = models.CharField(verbose_name=_("Заголовок"), max_length=100, blank=True)
    body = models.CharField(verbose_name=_("Текст"), max_length=2048, blank=True)

    class Meta:
        abstract = True


class Note(BaseArticle):
    tag = models.ManyToManyField(
        Tag,
        verbose_name=_('ссылка на тэг'),
        blank=True,
        related_name="tag_note",
        related_query_name="tag",
    )


class Article(BaseArticle):
    url = models.CharField(verbose_name=_("Ссылка на статью в интернете"), max_length=256, blank=True)
    tag = models.ManyToManyField(
        Tag,
        verbose_name=_('ссылка на тэг'),
        blank=True,
        related_name="tag_article",
        related_query_name="tag",
    )
