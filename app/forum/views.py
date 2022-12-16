from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    forum_list = models.Forum.objects.all()
    return render(request, "forum/index.html", {"forum_list": forum_list})


def forum_detail(request, pk):
    forum_data = models.Forum.objects.get(pk=pk)
    return render(request, "forum/forum-detail.html", {"forum_data": forum_data})

