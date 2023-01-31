from django.contrib.auth.models import User
from .models import File
from app.serializers import FileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class FileView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = [AllowAny]
    serializer_class = FileSerializer

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        return Response(FileSerializer(File.objects.all(), many=True).data)

    def post(self, request):
        print(request.data)
        print(request.FILES)
        data = FileSerializer(data=request.data)
        if data.is_valid():
            data.save()
        else:
            return Response({"err": "err"})

        return Response({"data": "Done"})
