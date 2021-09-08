from django.db.models import fields
from todo.models import Todo
from rest_framework import serializers
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'email', 'task', 'description', 'priority', 'created')

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email')
        instance.task = validated_data.get('task')
        instance.description = validated_data.get('description')
        instance.priority = validated_data.get('prioroity')
        instance.created = validated_data.get('created')
        instance.save()
        return instance



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'