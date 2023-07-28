from rest_framework import generics
from base.models import Show
from .serializers import ShowSerializer


class ShowList(generics.ListCreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class ShowDetail(generics.ListCreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
