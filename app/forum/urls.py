from django.urls import path
from forum import views

urlpatterns = [
    path("", views.index, name="forum-index"),
]