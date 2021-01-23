from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
# Create your views here.

class ListTodo(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # 記事一覧取得
    def list(self, request):
        data = TodoSerializer(Todo.objects.all().order_by('created_at').reverse(), many=True).data

        return Response(status=200, data=data) 

    # 記事詳細取得
    def retrieve(self, request, pk=None):
        todo_id = pk
        data = TodoSerializer(Todo.objects.filter(uuid=todo_id), many=True).data

        return Response(status=200, data=data)