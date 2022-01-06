from django.contrib.auth.models import User
from rest_framework import serializers
from chat.models import Message
from .models import *
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    """For Serializing User"""
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']
# 
# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=Registration.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=Registration.objects.all())
    class Meta:
        model = Message
        fields = '__all__'