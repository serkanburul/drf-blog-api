from django.db import models
from rest_framework.authtoken.admin import User
from blog.models import Post


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_by')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_post')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.user} liked {self.post}'


class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disliked_by')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='disliked_post')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.user} disliked {self.post}'

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorited_by')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorited_post')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.user} favorited {self.post}'
