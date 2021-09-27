from django.utils.translation import ugettext_lazy as _
from django.db import models
from accounts.models import User


class CreateDateMixin(models.Model):
    """ Дата создания """

    created_date = models.DateTimeField(
        verbose_name=_("Дата/время создания"),
        auto_now_add=True,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True


class UpdateDateMixin(models.Model):
    """ Дата изменения """

    update_date = models.DateTimeField(
        verbose_name=_("Дата/время изменения"),
        auto_now=True,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True


class UserMixin(models.Model):
    """ Ссылка на пользователя """

    user = models.ForeignKey(
        "accounts.User",
        verbose_name=_("Ссылка на Пользователя"),
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class DateMixin(CreateDateMixin, UpdateDateMixin):
    """ Поля связанные с датой """

    class Meta:
        abstract = True
