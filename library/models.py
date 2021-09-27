from django.utils.translation import ugettext_lazy as _

from django.db import models

from core.models import DateMixin, UserMixin


class Tag(DateMixin):
    tag_name = models.CharField(verbose_name=_("Тeг"), max_length=256, blank=True)

    def __str__(self):
        name = self.tag_name
        return f"{str(self.id)} {name}"

    class Meta:
        verbose_name = _("Тeг")
        verbose_name_plural = _("Тeги")


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
        related_query_name="tag_note",
    )

    def __str__(self):
        name = self.header
        return f"{str(self.id)} {name}"

    class Meta:
        verbose_name = _("Запись")
        verbose_name_plural = _("Записи")


class Article(BaseArticle):
    url = models.CharField(verbose_name=_("Ссылка на статью в интернете"), max_length=256, blank=True)
    tag = models.ManyToManyField(
        Tag,
        verbose_name=_('ссылка на тэг'),
        blank=True,
        related_name="tag_article",
        related_query_name="tag_article",
    )

    def __str__(self):
        name = self.header
        return f"{str(self.id)} {name}"

    class Meta:
        verbose_name = _("Статья")
        verbose_name_plural = _("Статьи")
