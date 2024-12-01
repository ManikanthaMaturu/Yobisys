from rest_framework import generics
from .models import SchemaSharedModel
from .serializers import SharedModelSerializer

class SharedModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = SchemaSharedModel.objects.all()
    serializer_class = SharedModelSerializer

class SharedModelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchemaSharedModel.objects.all()
    serializer_class = SharedModelSerializer
