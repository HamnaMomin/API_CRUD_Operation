from rest_framework import serializers
from .models import *
from rest_framework.fields import EmailField
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

    def create(self, validated_data):
        user = User.objects.create(username =validated_data['username'],email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #fields = ['name', 'age']
        fields = "__all__"
        

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError(
                {"error": "Age should be greater than 18 years"})

        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError(
                        {"error": "Name can not contain digit in it"})

        return data