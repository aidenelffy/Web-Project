from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view

from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework.request import Request
from rest_framework.response import Response

from ..models import Product,Furniture,Order
from api.serializers import ProductSerializer,FurnitureSerializer,OrderSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        product.delete()
        return Response({'message': 'deleted'}, status=204)





@api_view(['GET', 'POST'])
def furniture_list(request):
    if request.method == 'GET':
        furniture = Furniture.objects.all()
        serializer = FurnitureSerializer(furniture, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FurnitureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def furniture_detail(request, furniture_id):
    try:
        furniture = Furniture.objects.get(id=furniture_id)
    except Furniture.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = FurnitureSerializer(furniture)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FurnitureSerializer(instance=furniture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        furniture.delete()
        return Response({'message': 'deleted'}, status=204)


@csrf_exempt
def product_furniture(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error: ' + str(e)})
    furniture_list = product.furniture.all()
    furniture_json = [f.to_json() for f in furniture_list]

    if request.method == 'GET':
        return JsonResponse(furniture_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'added'})


@api_view(['GET', 'POST', 'DELETE'])
def orders_list(request):
    permission_classes = (IsAuthenticated,)
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        orders = Order.objects.all()
        orders.delete()

