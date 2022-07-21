from django.db import models
from django.conf import settings
import datetime
from django.contrib import admin



from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value

class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField(auto_now_add=True,  blank=True)
    modified_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts")
# This is only possible if it’s a model under your control, so we can use it to make fetching comments for a Post simple, but we can’t edit the User model so easily.
# Now fetching the Comments for a Post is simple. The comments attribute acts like a RelatedManager allowing you to query, filter(), add(), create() and remove() Comments to a Post. Let’s see a short example of how to use it.    
    comments = GenericRelation(Comment)
    

    def __str__(self):
        return self.title



