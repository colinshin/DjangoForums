from django.contrib import admin
from forum import models as forum_models


admin.site.register(forum_models.Forum)
