from rest_framework import serializers
from .models import TasksInfo

class TaskInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksInfo
        fields = '__all__'
