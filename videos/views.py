from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework import generics
from pytube import YouTube
import os
from psytube.pagination import CustomPageNumberPagination
from .models import Video
from .serializers import ListVideoDetailSerializer, VideoSerializer, VideoPostSerializer, ListTopVideoSerializer
import requests
from traitlets import Bool
import ipdb


class CreateVideoView(APIView):
    queryset = Video
    serializer_class = VideoPostSerializer

    def post(self, request):
        try:
            yt = YouTube(request.data["link"])
            if request.data.get("type") == "audio":
                video = yt.streams.filter(only_audio=True).last()
            else:
                video = yt.streams.filter(progressive=True).last()
            file_name = yt.title.replace('"', "'")
            video.download(output_path="./media", filename=f"{file_name}.mp4")
        except KeyError:
            return Response({"message": "invalid link"}, status.HTTP_400_BAD_REQUEST)
        my_file = open(f"./media/{file_name}.mp4", "rb")
        response = requests.post("https://file.io", files={"file": my_file})
        my_file.close()
        os.remove(f"./media/{file_name}.mp4")
        resposta = {
            "title": file_name,
            "thumbnail": yt.thumbnail_url,
        }
        serializer = VideoSerializer(data=resposta)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(link=request.data["link"])
        if Bool(request.user and request.user.is_authenticated):
            # ipdb.set_trace()
            instance.users.set(
                [*[user["id"] for user in serializer.data["users"]], request.user.id]
            )
        return Response(
            {
                **resposta,
                "link": request.data["link"],
                "download_url": response.json()["link"],
            },
            status.HTTP_200_OK,
        )


class ListTopVideosView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = ListTopVideoSerializer

    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return self.queryset.order_by("-downloads")[0:10]


class ListDetailVideosView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = ListVideoDetailSerializer

    pagination_class = CustomPageNumberPagination
