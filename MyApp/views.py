from functools import partial
from django.shortcuts import render
import pkg_resources

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import serializers
from django.http import Http404

from rest_framework.response import Response
from .models import Student
from django.contrib.auth.models import User
from .serializers import StudentSerializer, UserSerializer
from rest_framework import authentication

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed

# To show all student details


def MyHome(request):
    student_details = Student.objects.all()
    context = {'student_details': student_details, }
    return render(request, 'home.html', context)

# To register new user, access and refresh token also generated manually.


class RegisterUser(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({"status": 403, "errors": serializer.errors, "message": 'Something went wrong'})

        serializer.save()
        user = User.objects.get(username=serializer.data['username'])

        refresh = RefreshToken.for_user(user)

        return Response({"status": 200, 'payload': serializer.data, 'refresh': str(refresh),
                         'access': str(refresh.access_token), "message": 'Your data is saved'})

# for User login(JWT)


class LoginUser(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User does not found')

        if not user.check_password(password):
            raise AuthenticationFailed("Password is incorrect")

        refresh = RefreshToken.for_user(user)
        return Response({"message": "Login Success", 'refresh': str(refresh),
                         'access': str(refresh.access_token)})

# for logging out user(JWT)


class LogoutUser(APIView):

    def post(self, request):

        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({"status": 205, "message": "Logged out successfully"})


# Here Class based view is created
class StudentAPI(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk is not None:
            student_obj = self.get_object(pk)
            # get particular student detail using id
            serializer = StudentSerializer(student_obj)
            return Response(serializer.data)
        student_obj = Student.objects.all()  # provide all student detail
        serializer = StudentSerializer(student_obj, many=True)
        return Response(serializer.data)


# create new student record or post new sudent data here


    def post(self, request):
        data = request.data
        # print(data)
        serializer = StudentSerializer(data=request.data)

        """if request.data['age'] < 18:
            return Response({"status": 403,  "message": 'Age must be >18'}) """

        if not serializer.is_valid():
            return Response({"status": 403, "errors": serializer.errors, "message": 'Something went wrong'})

        serializer.save()
        return Response({"status": 200, 'payload': serializer.data, "message": 'Your data is saved'})

# update complete data of given student id
    def put(self, request, pk, format=None):
        try:
            id = pk
            student_obj = Student.objects.get(id=id)
            serializer = StudentSerializer(
                student_obj, data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({"status": 403, "errors": serializer.errors, "message": "Something went wrong"})

            serializer.save()
            return Response({"status": 200, 'payload': serializer.data,  "message": "Updated student data"})

        except Exception as e:
            print(e)
            return Response({"status": 403, "message": "Invalid Id"})

# update partial data of given student id
    def patch(self, request, pk, format=None):
        try:
            id = pk
            student_obj = Student.objects.get(id=id)
            serializer = StudentSerializer(
                student_obj, data=request.data,
                partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({"status": 403, "errors": serializer.errors, "message": "Something went wrong"})

            serializer.save()
            return Response({"status": 200, 'payload': serializer.data,  "message": "Updated student data partially"})

        except Exception as e:
            print(e)
            return Response({"status": 403, "message": "Invalid Id"})

# delete particular student data
    def delete(self, request, pk):
        try:
            id = pk
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({"status": 200, "message": "data delete"})
        except Exception as e:
            print(e)
            return Response({"status": 403, "message": "Invalid Id"})
