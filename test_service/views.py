from calendar import firstweekday
import re
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.parsers import MultiPartParser,JSONParser,FileUploadParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view,APIView,permission_classes
from django.contrib.auth.hashers import make_password,check_password
from rest_framework import generics
from django.contrib.auth import authenticate
from django.contrib.messages import constants as messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404, HttpResponseNotAllowed
from .models import *
from .urls import *
from .serializers import  *

# Create your views here.
class CreateUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        #validate serializer from CustomerRegSer..
        serializer = CustomerRegSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #if valid, send to CustomerSerializ...
        model_serializer = CustomerSerializer(data=serializer.data)
        model_serializer.is_valid(raise_exception=True)
        model_serializer.save()

        return Response(model_serializer.data, status=status.HTTP_201_CREATED)

#login endpoint
class LoginApiView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            first_name = request.data('first_name')
            password = request.data('password')
            user = authenticate(first_name=first_name, password=password)

            if user:
                try:
                    token = user.generate_token()# might have to remove this 
                    user_details = {}
                    user_details['id'] = "%d" % (user.id)
                    user_details['name'] = "%s %s" % (user.first_name, user.last_name)
                    user_details['token'] = token

                    return Response({'success':1,'msg': 'Login successful', 'user_details':user_details}, status=status.HTTP_200_OK)

                except:
                    return Response({'msg': 'Error while generating auhtenticating token.'}, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({'success':0, 'msg': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        except KeyError:
            return Response({'msg': 'Please provide a name and password'}, status=status.HTTP_401_UNAUTHORIZED)

#Create order endpoint
class CreateOrder(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        current_user = request.user
        data = request.data
        data.mutable = True
        data['customer']=1
        data.mutable = False

        order_serializer =  OrderSerializer(data=data)
        print(order_serializer)# check if it returns data
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#all orders endpoint
class AllOrders(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        order = Order.objects.all()
        current_user = self.request.user

        item = request.GET.get('item', None)
        if item is not None:
            item = Order.filter(item__icontains=item)

        order_serializer = OrderSerializer(item, many=True)
        return JsonResponse(order_serializer.data, safe=False)


#get/update/delete api








