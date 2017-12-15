from django.shortcuts import render
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from django.db import transaction
from django.db.utils import IntegrityError
from app.models.Address import Address
from app.models.Email import Email
from app.serializers import serializers
from app.models.PhoneNumber import PhoneNumber
from app.models.Person import Person
from rest_framework import viewsets

class PersonView(viewsets.ModelViewSet):

    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','firstName','lastName','birthday',)
        
class AddressView(viewsets.ModelViewSet):

    queryset = Address.objects.all()
    serializer_class = serializers.AddressSerializer

class PhoneNumberView(viewsets.ModelViewSet):

    queryset = PhoneNumber.objects.all()
    serializer_class = serializers.PhoneNumberSerializer

class EmailView(viewsets.ModelViewSet):

    queryset = Email.objects.all()
    serializer_class = serializers.EmailSerializer