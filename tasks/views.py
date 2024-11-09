from django.shortcuts import render
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    # It ensures that each user can only see their own tasks
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    

    # Automatically associate the task with the authenticated user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)