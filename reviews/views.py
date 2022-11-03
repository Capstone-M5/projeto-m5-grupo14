from rest_framework.generics import RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsAdmin_Or_ReviewOwner

# Create your views here.


@extend_schema(methods=["PUT"], exclude=True)
class RetrieveUpdateDestroyReviewView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdmin_Or_ReviewOwner]
