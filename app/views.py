from django.contrib.auth.models import User
from .models import File
from app.serializers import FileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import authentication


class FileView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer
    # authentication_classes = (authentication.BasicAuthentication,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        return Response(FileSerializer(File.objects.all(), many=True).data)

    def post(self, request):
        print()
        print("data")
        print(request.data)
        print("Files")
        print(request.FILES)
        print("Request")
        print(request)
        print("USer")
        print(request.user)
        print("Authorization header")
        print(request.headers.get('Authorization'))
        print("Meta")
        print(request.META)
        print()
        data = FileSerializer(data=request.data)
        if data.is_valid():
            data.user = request.user
            print(request.user)
            data.save(user=request.user)

        else:
            return Response({"err": "err"})

        return Response({"data": "Done"})
