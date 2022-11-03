from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from videos.models import Video
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsAdmin_Or_ReviewOwner
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ListCreateReview(ListCreateAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(video_id=self.kwargs['pk'], user=self.request.user)

class RetrieveUpdateDestroyReviewView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdmin_Or_ReviewOwner]
