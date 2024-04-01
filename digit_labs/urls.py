from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path(f"{settings.API_VERSION}/", include("app.urls")),
]
