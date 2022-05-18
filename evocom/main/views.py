from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import About_UsSerializer, Choose_UsSerializer, Our_ServicesSerializer, ServicesSerializer,PartnersSerializer,ContactsSerializer
  
from .models import *


class About_UsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        about_us = About_Us.objects.all()
        about_us_json = About_UsSerializer(about_us, many=True)
        return Response(data=about_us_json.data)


class Choose_UsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        choose_us = Choose_Us.objects.all()
        choose_us_json = Choose_UsSerializer(choose_us, many=True)
        return Response(data=choose_us_json.data)



class Our_ServicesListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        our_services = Our_Services.objects.all()
        our_services_json = Our_ServicesSerializer(our_services, many=True)
        return Response(data=our_services_json.data)



class ServicesListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        services = Services.objects.all()
        services_json = ServicesSerializer(services, many=True)
        return Response(data=services_json.data)



class PartnersListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        partners = Partners.objects.all()
        partners_json = PartnersSerializer(partners, many=True)
        return Response(data=partners_json.data)



class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

    