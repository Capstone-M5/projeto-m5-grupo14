from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework import generics
from pytube import YouTube
from .models import Video
from .serializers import VideoSerializer
import requests

# Create your views here.


class CreateVideoView(APIView):
    def post(self, request):
        yt = YouTube(request.data["link"])
        video = yt.streams.filter(progressive=True).last()
        video.download(output_path="./media", filename="video")
        my_file = open("./media/video", "rb")
        response = requests.post(
            "https://file.io", files={"file": my_file})
        my_file.close()
        return Response({"title": yt.title, "download_url": response.json()["link"], "video_url": request.data["link"], "author": yt.author}, status.HTTP_200_OK)


class ListTopVideosView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        return self.queryset.order_by("downloads")[0:10]
        ...

    ...
