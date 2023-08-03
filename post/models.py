from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


def post_photo_path(post, filename):
    return f'posts/photos/{filename}'


class Post(models.Model):
    content = models.TextField()
    photo = models.ImageField(max_length=500, upload_to=post_photo_path, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self) -> str:
        return self.pk
    

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

