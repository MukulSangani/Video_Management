from .models import Video
from django.db.models import Q

class VideoManager:
    def __init__(self):
        self.videos = Video.objects.all()

    def get_video(self, video_id):
        return self.videos.get(id=video_id)

    def search_videos(self, query):
        return self.videos.filter(Q(title__icontains=query) | Q(size__icontains=query))