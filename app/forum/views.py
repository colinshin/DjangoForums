from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    forum_cat_list = models.ForumCategory.objects.all()
    return render(request, "forum/index.html", {"forum_cat_list": forum_cat_list})


def forum_category_detail(request, pk):
    forum_cat_data = models.ForumCategory.objects.get(pk=pk)
    return render(request, "forum/forum-category-detail.html", {"cat_data": forum_cat_data})


def forum_detail(request, pk):
    forum_data = models.Forum.objects.get(pk=pk)
    return render(request, "forum/forum-detail.html", {"forum_data": forum_data})

