from django.contrib import admin
from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
from rest_framework import routers
from eventFinderApp import viewsets
from rest_framework.authtoken import views
from users import viewsets as UserViewsets

router = routers.DefaultRouter()
router.register(r"events", viewsets.EventViewSet)
router.register(r"users", UserViewsets.CustomUserViewSet)

urlpatterns = [
    path("event-finder/", include("eventFinderApp.urls")),
    path("admin/", admin.site.urls),
    path("users/", include("django.contrib.auth.urls")),
    path("users/", include("users.urls")),
    path("api/", include(router.urls)),
    path(r"api-auth-token/", views.obtain_auth_token),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]
