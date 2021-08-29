from rest_framework import serializers
from CollectionApp.models import Bin, Operation, Collection

class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = ("id", "latitude", "longitude")

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ("id", "name")

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ("id", "bin", "operation", "collection_frequency", "last_collection")
