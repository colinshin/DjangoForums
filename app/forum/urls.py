from django.urls import path
from forum import views

urlpatterns = [
    path("", views.index, name="forum-index"),
    path("forum/<int:pk>/", views.forum_detail, name="forum-detail"),
    path("forum-category/<int:pk>/", views.forum_category_detail, name="forum-category-detail"),
]
