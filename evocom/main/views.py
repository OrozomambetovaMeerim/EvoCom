from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import About_UsSerializer
from .models import *


class About_UsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        about_us = About_Us.objects.all()
        about_us_json = About_UsSerializer(about_us, many=True)
        return Response(data=about_us_json.data)
