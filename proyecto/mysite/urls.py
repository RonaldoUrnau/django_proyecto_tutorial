from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponseRedirect

urlpatterns = [
    path("polls/", include("polls.urls")),  # URLs para la app polls
    path("", lambda request: HttpResponseRedirect("polls/")),  # Redirige la raíz a /polls/
    path("admin/", admin.site.urls),  # URL para el admin
]
