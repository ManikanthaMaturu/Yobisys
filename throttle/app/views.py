from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import ScopedRateThrottle
from .models import UserModel
from .serializers import UserModelSerializer
from .throttles import CustomThrottle
# views.py
from rest_framework import generics
from .models import UserModel
from .serializers import UserModelSerializer

class UserCreateView(generics.CreateAPIView):
    """
    API to create a new user (POST).
    """
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


from rest_framework import generics
from .models import UserModel
from .serializers import UserModelSerializer
from .throttles import CustomThrottle  

class UserListView(generics.ListAPIView):
    """
    API to retrieve all users (GET) with throttling applied.
    """
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    throttle_classes = [CustomThrottle]