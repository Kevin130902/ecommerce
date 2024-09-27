from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Produto
from .serializers import ProdutoSerializer

@api_view(["GET", "POST"])
def list_products(request):
    if request.method == "GET":
        queryset = Produto.objects.all()
        serializer = ProdutoSerializer(queryset, many=True)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProdutoSerializer(data=request.data)
        responseStatus = status.HTTP_400_BAD_REQUEST

        if serializer.is_valid():
            serializer.save()
            responseStatus = status.HTTP_201_CREATED

        return Response(serializer.data, status=responseStatus)