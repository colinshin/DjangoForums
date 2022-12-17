from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class ForumCategory(BaseModel):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Forum(BaseModel):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.category.name}"

    class Meta:
        unique_together = ("name", "category")


class ForumPost(BaseModel):
    title = models.CharField(max_length=256)
    views = models.IntegerField(default=0)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
