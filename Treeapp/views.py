from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .Serializer import CategorySerializer
from rest_framework.response import Response

# Create your views here.


class CategoryView(viewsets.ModelViewSet):
   
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            print("Queryset:", queryset)  # Print the queryset to check data
            serializer = self.get_serializer(queryset, many=True)
            print("Serialized Data:", serializer.data)  # Print serialized data
            return Response(serializer.data)