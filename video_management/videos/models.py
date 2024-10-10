# videos/models.py
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    # id = models.PositiveSmallIntegerField()
    # size=models.PositiveIntegerField()
    is_blocked = models.BooleanField(default=True)

class Blocklist(models.Model):
    video_id=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
