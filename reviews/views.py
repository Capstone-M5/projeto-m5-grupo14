from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsAdmin_Or_ReviewOwner
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class RetrieveUpdateDestroyReviewView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdmin_Or_ReviewOwner]
