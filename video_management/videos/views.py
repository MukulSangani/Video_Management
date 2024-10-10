# videos/views.py
from http.client import HTTPResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Video
from rest_framework.decorators import api_view
from .serializers import VideoSerializer
from django.conf import settings
from .models import Blocklist

from .utils import convert_video_to_mp4
from django.shortcuts import render,redirect
from django.db.models import Q

def home(request):
    return redirect('video-upload-form') 


    

class VideoSearchView(APIView):
    def get(self, request):
        query = request.GET.get('query')
        videos = Video.objects.filter(Q(title__icontains=query) | Q(size__icontains=query))
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

class BlocklistView(APIView):
    def post(self, request):
        video_id = request.POST['video_id']
        Blocklist.objects.create(video_id=video_id)
        return Response({'message': 'Video blocked successfully'})

class VideoUploadView(APIView):
    def post(self, request):
        try:
            video_file = request.FILES['video_file']
            video = Video.objects.create(title=request.POST['title'], video_file=video_file)
            convert_video_to_mp4(video.video_file.path)
            serializer = VideoSerializer(video)
            return Response(serializer.data)
        except KeyError:
            return Response({"detail": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)