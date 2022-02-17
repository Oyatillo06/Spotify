

from django.contrib import admin
from django.urls import path, include
from musicapp.views import SongViewSet,ArtisViewSet,AlbumViewSet
from rest_framework.routers import DefaultRouter


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Spotify clone API",
      default_version='v1',
      description="Spotify clone versiyasi Django Rest Framework va Postgresqldan foydalangan",
      contact=openapi.Contact("Oyatillo Sharobiddinov <contact@snippets.local>,<+998900403317>"),
   ),
   public=True,
)

router=DefaultRouter()
router.register('song',SongViewSet)
router.register('artis',ArtisViewSet)
router.register('album',AlbumViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('docs/',schema_view.with_ui("swagger",cache_timeout=0),name="swagger-doc"),
    path('docs2/',schema_view.with_ui("redoc",cache_timeout=0),name="redoc"),


]
