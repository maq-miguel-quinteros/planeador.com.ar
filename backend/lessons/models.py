from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    applicated_at = models.DateTimeField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE(), related_name='lessons')

    def __srt__(self):
        return self.title
