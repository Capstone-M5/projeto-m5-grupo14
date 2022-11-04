from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsAdmin_Or_ReviewOwner
from django.shortcuts import get_object_or_404
from videos.models import Video
from rest_framework.views import status
from rest_framework.response import Response
from django.core.exceptions import ValidationError


class ListCreateReview(ListCreateAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        video = get_object_or_404(Video, id=self.kwargs['pk'])
        serializer.save(video_id=video.__dict__[
            "id"], user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except ValidationError:
            return Response({"detail": "Video id must be an UUID."}, status.HTTP_400_BAD_REQUEST)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@extend_schema(methods=["PUT"], exclude=True)
class RetrieveUpdateDestroyReviewView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdmin_Or_ReviewOwner]
