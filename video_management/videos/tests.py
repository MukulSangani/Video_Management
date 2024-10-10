from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Video

class VideoTests(APITestCase):
    def test_upload_video(self):
        with open('C:/Users/admin/Downloads/file_example_MOV_480_700kB_converted.mp4', 'rb') as video:
            response = self.client.post(reverse('upload_video'), {'video': video})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_search_video(self):
        Video.objects.create(title='mukul1', id=14)
        response = self.client.get(reverse('search_video'), {'title': 'mukul1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
