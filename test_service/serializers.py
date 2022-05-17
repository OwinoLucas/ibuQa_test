from rest_framework import serializers,status
from test_service.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import User


class CustomerSerializer(serializers.ModelSerializer):
 
    date_joined = serializers.ReadOnlyField()# do i really need this?
 
    class Meta(object):
        model = User #import built in django user
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class CustomerRegSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField()
    confirm_password = serializers.CharField()


    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")

        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
          
        return data

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'