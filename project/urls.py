from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from welcome.views import index, health, hello

urlpatterns = [
    path("", index, name="index"),
    path("health", health, name="health"),
    path("admin/", admin.site.urls),
    path("hello", hello, name="hello"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

