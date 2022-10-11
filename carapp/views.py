from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import carlistSerializer
from .models import carlist


# Create your views here.

"""@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>/',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>/',
        'Delete': '/product-detail/<int:id>/',
    }
    return Response(api_urls);
"""

@api_view(['GET'])
def ShowAll(request):
    product = carlist.objects.all()
    serializer = carlistSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewModel(request, pk):
    product = carlist.objects.get(id=pk)
    serializer = carlistSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateModel(request):
    serializer = carlistSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateModel(request, pk):
    product = carlist.objects.get(id=pk)
    serializer = carlistSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteModel(request, pk):
    product = carlist.objects.get(id=pk)
    product.delete()

    return Response('Items delete successfully!')
from django.shortcuts import render

# Create your views here.
