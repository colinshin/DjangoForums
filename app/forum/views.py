from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    forum_list = models.Forum.objects.all()
    return render(request, "forum/index.html", {"forum_list": forum_list})

