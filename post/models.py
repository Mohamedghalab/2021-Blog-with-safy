from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator


class Category(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return str(self.name)
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
       
    def comments_count(self):
        return Comment.objects.filter(post=self, active=True).count()


class Comment(models.Model):
    comment = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.created_by} commented on {self.post}"
    
