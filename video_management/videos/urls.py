# videos/urls.py
from django.urls import path
from .views import VideoSearchView,VideoUploadView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
   path('upload/', VideoUploadView.as_view(), name='upload_video'),
    path('search/', VideoSearchView.as_view(), name='search_video'),
    # path('download/<int:video_id>/', download_video, name='download_video'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)