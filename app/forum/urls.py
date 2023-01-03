from django.urls import path
from forum import views

urlpatterns = [
    path("", views.index, name="forum-index"),
    path("forum/<int:pk>/", views.forum_detail, name="forum-detail"),
    path("forum-category/<int:pk>/", views.forum_category_detail, name="forum-category-detail"),
    path("forum/<int:pk>/new-topic/", views.new_forum_topic, name="forum-new-topic"),
    path("forum/<int:pk>/post/<int:post_pk>/", views.post_detail, name="forum-post-detail"),
]
