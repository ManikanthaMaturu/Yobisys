

from rest_framework import serializers
from .models import SchemaSharedModel

class SharedModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemaSharedModel
        fields = ['id', 'name', 'description', 'created_at']
