from django.shortcuts import render, redirect
from . import models
from . import forms as post_forms

# Create your views here.
def index(request):
    forum_cat_list = models.ForumCategory.objects.all()
    return render(request, "forum/index.html", {"forum_cat_list": forum_cat_list})


def forum_category_detail(request, pk):
    forum_cat_data = models.ForumCategory.objects.get(pk=pk)
    return render(request, "forum/forum-category-detail.html", {"cat_data": forum_cat_data})


def forum_detail(request, pk):
    forum_data = models.Forum.objects.get(pk=pk)
    post_list = models.ForumPost.objects.filter(forum=forum_data, parent__isnull=True)
    return render(request, "forum/forum-detail.html", {"forum_data": forum_data, "post_list": post_list})


def new_forum_topic(request, pk):
    forum_data = models.Forum.objects.get(pk=pk)
    if request.method == "POST":
        title = request.POST.get("topic-title", None)
        content = request.POST.get("topic-content", None)

        new_topic = models.ForumPost(
            title=title,
            content=content,
            author=request.user,
            forum=forum_data,
            parent=None
        )
        new_topic.save()
        return redirect("forum-detail", pk)
    return render(request, "forum/new-forum-topic.html", {"forum_data": forum_data})
 

def post_detail(request, pk, post_pk):
    forum_data = models.Forum.objects.get(pk=pk)
    post_data = models.ForumPost.objects.get(pk=post_pk)
    reply_list = models.ForumPost.objects.filter(forum=forum_data, parent=post_data).order_by("created_at")
    if request.method == "POST":
        form = post_forms.PostForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.forum = forum_data
            item.parent = post_data
            item.save()
            return redirect("forum-detail", item.id)
    else:
        form = post_forms.PostForm()
    return render(
        request,
        "forum/post-detail.html",
        {"forum_data": forum_data, "post_data": post_data, "form": form, "reply_list": reply_list}
    )
