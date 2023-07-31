from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    DjangoModelPermissionsOrAnonReadOnly,
    BasePermission,
    SAFE_METHODS,
)
from base.models import Show
from .serializers import ShowSerializer


class AdminWritePermission(BasePermission):
    message = "Editing the list is restricted to user list only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return request.user == obj.user_id


class IndexView(APIView):
    """Default View checked when at the index of a file"""

    def get(self, request, format=None):
        """Returns information about the API endpoints"""

        return Response()


class ShowList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class ShowDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminWritePermission]
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
