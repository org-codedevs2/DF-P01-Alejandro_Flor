from django.urls import path
from . import views

app_name = "suma"

urlpatterns = [
    path("", views.sumar, name="sumar"),
]