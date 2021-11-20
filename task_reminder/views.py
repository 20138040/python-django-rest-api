from django.shortcuts import render
from rest_framework.views import APIView
from .models import TodoTask
from .serializers import TodoTaskSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ToDoAPI(APIView):
    """
    List all article, or create a new snippet.
    """
    def get(self, request, format=None):
        task = TodoTask.objects.all()
        serializer = TodoTaskSerializer(task, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
