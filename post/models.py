from django.db import models
from user.models import User


# Create your models here.

class Post(models.Model):
    text = models.TextField("Текст", null=True)
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    created_at = models.DateField(auto_now_add=True)
    content = models.TextField("Комментарий")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.content}"[:100]


class Rate(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="marks")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_marks")
    value = models.IntegerField("Оценка")
    created_at = models.DateTimeField(auto_now_add=True)
