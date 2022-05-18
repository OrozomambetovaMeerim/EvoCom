from rest_framework import serializers
from .models import *


class About_UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Us
        fields = '__all__'


class Choose_UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choose_Us
        fields = '__all__'



class Our_ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_Services
        fields = '__all__'



class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'



class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'



class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'  