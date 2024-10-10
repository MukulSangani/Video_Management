from .models import Blocklist

class BlocklistManager:
    def __init__(self):
        self.blocklist = Blocklist.objects.all()

    def is_video_blocked(self,video_id):
        return video_id in self.blocklist