from django.shortcuts import render, redirect
from django.core.paginator import Paginator
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
    per_page = 3
    post_list = models.ForumPost.objects.filter(forum=forum_data, parent__isnull=True)
    paginator = Paginator(post_list, per_page)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    return render(
        request,
        "forum/forum-detail.html",
        {"forum_data": forum_data, "post_list": page_obj}
    )


def new_forum_topic(request, pk):
    forum_data = models.Forum.objects.get(pk=pk)
    if request.method == "POST":
        form = post_forms.PostForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.forum = forum_data
            item.parent = None
            item.save()
            return redirect("forum-detail", pk)
    else:
        form = post_forms.PostForm()
    return render(request, "forum/new-forum-topic.html", {"forum_data": forum_data, "form": form})


def post_detail(request, pk, post_pk):
    forum_data = models.Forum.objects.get(pk=pk)
    post_data = models.ForumPost.objects.get(pk=post_pk)
    reply_list = models.ForumPost.objects.filter(
        forum=forum_data,
        parent=post_data
    ).order_by("created_at")
    if request.method == "POST":
        form = post_forms.PostForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.forum = forum_data
            item.parent = post_data
            item.save()
            return redirect("forum-post-detail", pk=pk, post_pk=post_pk)
    else:
        form = post_forms.PostForm()
    return render(
        request,
        "forum/post-detail.html",
        {"forum_data": forum_data, "post_data": post_data, "form": form, "reply_list": reply_list}
    )
