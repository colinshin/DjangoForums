from django.shortcuts import render, redirect
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


def new_forum_topic(request, pk):
    forum_data = models.Forum.objects.get(pk=pk)
    if request.method == "POST":
        title = request.POST.get("topic-title", None)
        content = request.POST.get("topic-content", None)

        new_topic = models.ForumPost(title=title, content=content, author=request.user)
        new_topic.save()
        return redirect("forum-detail", pk)
    return render(request, "forum/new-forum-topic.html", {"forum_data": forum_data})
 
