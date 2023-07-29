import io
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from .serializers import TaskInfoSerializer
from .models import TasksInfo
# Create your views here.

@csrf_exempt
def tasksApi(request, id=0):
    if request.method == 'GET':
        task = TasksInfo.objects.all()
        task_serializer = TaskInfoSerializer(task, many=True)
        return JsonResponse(task_serializer.data, safe = False)
    
    if request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TaskInfoSerializer(data = task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse("Task Added", safe=False)
        return JsonResponse("Failed to Add the task", safe=False)
    
    if request.method == 'PUT':
        task_data = JSONParser().parse(request)
        task = TasksInfo.objects.get(id=id)
        task_serializer = TaskInfoSerializer(task, data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse("Updated!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    if request.method == 'DELETE':
        task = TasksInfo.objects.get(id=id)
        task.delete()
        return JsonResponse("Deleted", safe=False)
    
def working(request):
    return HttpResponse("Backend Working....")