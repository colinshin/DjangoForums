from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class ForumCategory(BaseModel):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Forum(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=512)
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

