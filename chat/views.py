from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User                                # Django Build in User Model
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from chat.models import Message      
from rest_framework.response import Response
from rest_framework import status                                             # Our Message model
from chat.serializers import MessageSerializer, UserSerializer # Our Serializer Classes
from rest_framework.views import APIView
# Users View

class  MessageList(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = MessageSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

         
        except Exception as e:
            print(e)
            return Response(data='somthing went wrong',status=status.HTTP_400_BAD_REQUEST)


    def get(self,request):
        try:
            username = request.GET.get('username')
            if username is None:
                return Response(data="username is not Empty")
            else:
                obj = Message.objects.filter(sender__username = username) | Message.objects.filter(receiver__username=username)
                serializer = MessageSerializer(obj,many=True,context={'request':request})
                return Response(data=serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data='somthing went wrong',status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        try:
            username = request.GET.get('username')
            message_id=request.GET.get('id')
            print(username,message_id)
            if username is None:
                return Response(data="username is not Empty")
            else:
                obj = Message.objects.filter(sender__username = username,id=int(message_id)) | Message.objects.filter(receiver__username=username,id=int(message_id))
                obj.delete()
                return Response(data="delete successfully",status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data='somthing went wrong',status=status.HTTP_400_BAD_REQUEST)
