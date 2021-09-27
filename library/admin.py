from django.apps import apps
from django.contrib import admin

from .apps import app_name

app_models = apps.get_app_config(app_name).get_models()
admin.site.register(app_models)

