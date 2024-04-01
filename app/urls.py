from django.urls import path
from app.locker_view import insert_locker, update_locker
from app.defination_view import insert_definition, update_definition

urlpatterns = [
    path("locker/", insert_locker, name="insert-locker"),
    path("locker/<str:id>/", update_locker, name="update-locker"),

    path("definition/", insert_definition, name="insert-definition"),
    path("definition/<str:id>/", update_definition, name="update-definition")
]
