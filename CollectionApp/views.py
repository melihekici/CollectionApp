from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CollectionApp.models import Bin, Operation, Collection
from CollectionApp.serializers import BinSerializer, OperationSerializer, CollectionSerializer

# Create your views here.


@csrf_exempt
def BinApi(request, id=0):
    if request.method == "GET":
        bins = Bin.objects.all()
        bins_serializer = BinSerializer(bins, many=True)
        return JsonResponse(bins_serializer.data, safe=False)
    elif request.method == "POST":
        bins_data = JSONParser().parse(request)
        bins_serializer = BinSerializer(data=bins_data)
        if bins_serializer.is_valid():
            bins_serializer.save()
            return JsonResponse("Bin added successfuly.", safe=False)
        return JsonResponse(f"Failed to add.{bins_serializer._errors}", safe=False)
    elif request.method == "PUT":
        bins_data = JSONParser().parse(request)
        current_bin = Bin.objects.get(id=bins_data["id"])
        bins_serializer = BinSerializer(current_bin, data=bins_data)
        if bins_serializer.is_valid():
            bins_serializer.save()
            return JsonResponse("Updated succesfuly", safe=False)
        return JsonResponse(f"Failed to update.{bins_serializer._errors}", safe=False)
    elif request.method == "DELETE":
        current_bin = Bin.objects.get(id=id)
        current_bin.delete()
        return JsonResponse("Deleted successfuly.", safe=False)

@csrf_exempt
def OperationApi(request, id=0):
    if request.method == "GET":
        operations = Operation.objects.all()
        operations_serializer = OperationSerializer(operations, many=True)
        return JsonResponse(operations_serializer.data, safe=False)
    elif request.method == "POST":
        operations_data = JSONParser().parse(request)
        operations_serializer = OperationSerializer(data=operations_data)
        if operations_serializer.is_valid():
            operations_serializer.save()
            return JsonResponse("Operation added successfuly.", safe=False)
        return JsonResponse(f"Failed to add.{operations_serializer._errors}", safe=False)
    elif request.method == "PUT":
        operation_data = JSONParser().parse(request)
        operation = Operation.objects.get(id=operation_data["id"])
        operations_serializer = OperationSerializer(operation, data=operation_data)
        if operations_serializer.is_valid():
            operations_serializer.save()
            return JsonResponse("Updated operation successfuly.", safe=False)
        return JsonResponse(f"Failed to update.{operations_serializer._errors}", safe=False)
    elif request.method == "DELETE":
        operation = Operation.objects.get(id=id)
        operation.delete()
        return JsonResponse("Deleted operation successfuly.", safe=False)

@csrf_exempt
def CollectionApi(request, id=0):
    if request.method == "GET":
        collections = Collection.objects.all()
        collections_serializer = CollectionSerializer(collections, many=True)
        return JsonResponse(collections_serializer.data, safe=False)
    elif request.method == "POST":
        collection_data = JSONParser().parse(request)
        collections_serializer = CollectionSerializer(data=collection_data)
        if collections_serializer.is_valid():
            collections_serializer.save()
            return JsonResponse("Collection added successfuly.", safe=False)
        return JsonResponse(f"Failed to add.{collections_serializer._errors}", safe=False)
    elif request.method == "PUT":
        collection_data = JSONParser().parse(request)
        collection = Collection.objects.get(id=collection_data["id"])
        collections_serializer = CollectionSerializer(collection, data=collection_data)
        if collections_serializer.is_valid():
            collections_serializer.save()
            return JsonResponse("Updated collection successfuly.", safe=False)
        return JsonResponse(f"Failed to update.{collections_serializer._errors}", safe=False)
    elif request.method == "DELETE":
        collection = Collection.objects.get(id=id)
        collection.delete()
        return JsonResponse("Deleted collection successfuly.", safe=False)
