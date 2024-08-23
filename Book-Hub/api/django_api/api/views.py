from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import AllowAny


class BookCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [AllowAny]

class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookDetails(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookUpdate(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookSearch(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get_queryset(self):
        name = self.kwargs.get('title')
        return Book.objects.filter(title__icontains=name)
    

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny]

class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserSearch(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_queryset(self):
        name = self.kwargs.get('name')
        return User.objects.filter(name__icontains=name)