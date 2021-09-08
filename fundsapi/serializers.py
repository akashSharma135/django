from django.db.models import fields
from rest_framework import serializers
from .models import AMC, Nav, Scheme

class AMCSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMC
        fields = ['name']

class SchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheme
        fields = '__all__'

class NavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nav
        fields = ['scheme', 'nav', 'date']