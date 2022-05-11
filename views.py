from django.shortcuts import render
from rest_framework import status
from shop.models import Category
from shop.models import Customer
from shop.models import Order
from shop.models import ChekoutDetail
from shop.serializers import CategorySerializer
from shop.serializers import CustomerSerializer
from shop.serializers import OrderSerializer
from shop.serializers import ChekoutDetail
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def category_list(request):
    if request.method=='GET':
        categorys=Category.objects.all()
        categorys_serializer=CategorySerializer(categorys,many=True)
        return Response(categorys_serializer.data)
    elif request.method=='POST' :
        category_serializer=CategorySerializer(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data,status=status.HTTP_201_CREATED)
        return Response(category_serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET','PUT','DELETE'])
def cagetory_detail(request,pk):
   if request.method=='GET':
       category_serializer=CategorySerializer(category)
       return Response(category_serializer.data)
   elif request.method=='PUT':
        catgeory_serializer=CategorySerializer(category,datat=request.data)
        if category_serializer.is_valid():
            catgeory_serializer.save()
            return Response(category_serializer.data)
        return Response(category_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
   elif request.method == 'DELETE':
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
