from rest_framework import routers

from django.urls import include, path

from . import views

router = routers.DefaultRouter()

router.register('event', views.EventViewSet, basename='event')
router.register('access_type', views.Access_typeViewSet, basename='access_type')
router.register('adresse', views.AdresseViewSet, basename='adresse')
router.register('audience', views.AudienceViewSet, basename='audience')
router.register('group', views.GroupViewSet, basename='group')
router.register('occurrence', views.OccurrenceViewSet, basename='occurrence')
router.register('price_type', views.Price_typeViewSet, basename='price_type')
router.register('tag', views.TagViewSet, basename='tag')

urlpatterns = [
    path('', include(router.urls)),
]