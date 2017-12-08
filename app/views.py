from django.shortcuts import render
from app.models.Email import Email
from app.serializers import serializers
from app.models.PhoneNumber import PhoneNumber
from app.models.Address import Address
from app.models.Person import Person
from rest_framework import viewsets
from datetime import datetime

class PersonView(viewsets.ModelViewSet):

    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer

class AddressView(viewsets.ModelViewSet):

    queryset = Address.objects.all()
    serializer_class = serializers.AddressSerializer

class PhoneNumberView(viewsets.ModelViewSet):

    queryset = PhoneNumber.objects.all()
    serializer_class = serializers.PhoneNumberSerializer

class EmailView(viewsets.ModelViewSet):

    queryset = Email.objects.all()
    serializer_class = serializers.EmailSerializer