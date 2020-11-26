from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Entry(models.Model):
    entry_title = models.CharField(max_length=50)
    #entry_text = models.TextField()
    entry_text = RichTextField(null=True, blank=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_image = models.ImageField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='blog_likes')#related_name='blog_likes'不知道啥功能

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.entry_title

class Comment(models.Model):
    comment_name = models.CharField(max_length=50)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_entry = models.ForeignKey(Entry, on_delete=models.CASCADE)