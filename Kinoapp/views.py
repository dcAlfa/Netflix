from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


# class KinolarAPIView(APIView):
#     def get(self,request):
#         kinolar = Kino.objects.all()
#         ser = Kinoserializers(kinolar, many=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#
#
#
#
#
# class AktyorlarAPIView(APIView):
#     def get(self,request):
#         aktyorlar = Aktyor.objects.all()
#         ser = Aktyorserializers(aktyorlar, many=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#

class AktyorViewSet(ModelViewSet):
    queryset = Aktyor.objects.all()
    serializer_class = Aktyorserializers
    @action(detail=True, methods=['get','post'])
    def kinolar(self, request, pk=None):
        if request.method=="POST":
            malumot = request.data
            ser = Kinoserializers(data=malumot)
            if ser.is_valid():
                ser.save()
                oxirgi = Kino.objects.last()
                oxirgi.aktyorlar = self.get_object()
                oxirgi.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        aktyor = self.get_object()
        kino = Kino.objects.filter(aktyorlar=aktyor)
        ser = Kinoserializers(kino, many=True)
        return Response(ser.data)


class KinoViewSet(ModelViewSet):
    queryset = Kino.objects.all()
    serializer_class = Kinoserializers
