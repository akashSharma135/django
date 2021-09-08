from django.db.models import fields, manager
from rest_framework import response
from rest_framework import serializers
from django.core import serializers
from rest_framework.serializers import Serializer
from .serializers import NavSerializer, SchemeSerializer, AMCSerializer
from .models import AMC, Nav, Scheme
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
import json

class AMCView(APIView):
    def get(self, request, format=None):
        try:
            scheme = AMC.objects.all()
            serializer = AMCSerializer(scheme, many=True)
            return Response(serializer.data, status=200)
        except AMC.DoesNotExist:
            pass


    def post(self, request, format=None):
        serializer = AMCSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SchemeView(APIView):

    def get(self, request, format=None):
        try:
            scheme = Scheme.objects.all()
            serializer = SchemeSerializer(scheme, many=True)
            return Response(serializer.data, status=200)
        except Scheme.DoesNotExist:
            pass


    def post(self, request, format=None):
        serializer = SchemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        

class NavView(APIView):

    def get(self, request, format=None):
        try:
            nav = Nav.objects.all()
            serializer = NavSerializer(nav, many=True)
            print(serializer.data)
            return Response(serializer.data, status=200)
        except Nav.DoesNotExist:
            pass


    def post(self, request, format=None):
        serializer = NavSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    
        
        

class NavDetailView(APIView):
    def get(self, request, id):
        try:
            nav = Nav.objects.filter(pk=id)
            serializer = NavSerializer(nav, many=True)
            print(serializer.data)
            return Response(serializer.data, status=200)
        except Nav.DoesNotExist:
            pass
        
        
        