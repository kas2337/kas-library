from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticlesViews, NotesViews, TagsViews

router = DefaultRouter()
router.register(
    r"articles",
    ArticlesViews,
    basename="articles",
)
router.register(
    r"notes",
    NotesViews,
    basename="notes",
)
router.register(
    r"tags",
    TagsViews,
    basename="tags",
)

urlpatterns = [
    path("", include(router.urls)),
]
