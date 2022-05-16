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
def home(request):
   
    context = { }
    return render(request, 'index.html', context)