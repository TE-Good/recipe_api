from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

# Router automatically generates URLS for viewsets
# I assume depending list/detail and view names
router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
  # direct all urls into our router
  path('', include(router.urls))
]
