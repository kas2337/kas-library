from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            return ValueError("Необходимо указать почту")

        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name=_("Псевдоним"), max_length=100, blank=True)
    email = models.EmailField(verbose_name=_("Электронная почта"), unique=True)
    first_name = models.CharField(verbose_name=_("Имя"), max_length=100, blank=True)
    last_name = models.CharField(verbose_name=_("Фамилия"), max_length=100, blank=True)
    created_date = models.DateTimeField(verbose_name=_("Дата регистрации"), auto_now_add=True)
    is_active = models.BooleanField(verbose_name=_("Активна"), default=True)
    is_staff = models.BooleanField(_("Статус Администратора"), default=False,)
    is_superuser = models.BooleanField(_("Статус Администратора"), default=False,)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"
