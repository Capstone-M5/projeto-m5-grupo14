
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsAdmin_Or_ReviewOwner

# Create your views here.


class ListCreateReview(ListCreateAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(video_id=self.kwargs['pk'], user=self.request.user)


@extend_schema(methods=["PUT"], exclude=True)
class RetrieveUpdateDestroyReviewView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdmin_Or_ReviewOwner]
