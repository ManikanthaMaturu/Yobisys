from django.urls import path
from .views import  SharedModelListCreateAPIView, SharedModelRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('shared-models/', SharedModelListCreateAPIView.as_view(), name='shared-models-list-create'),
    path('shared-models/<int:pk>/', SharedModelRetrieveUpdateDestroyAPIView.as_view(), name='shared-models-detail'),
]