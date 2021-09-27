from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'
    verbose_name = _("Библиотека")


app_name = LibraryConfig.name
