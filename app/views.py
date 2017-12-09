from django.shortcuts import render
from app.models.Address.Address import Address
from app.models.Address.City import City
from app.models.Address.State import State
from app.models.Email import Email
from app.serializers import serializers
from app.models.PhoneNumber import PhoneNumber
from app.models.Person import Person
from rest_framework import viewsets
from datetime import datetime

class PersonView(viewsets.ModelViewSet):

    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer


class StateView(viewsets.ModelViewSet):

    queryset = State.objects.all()
    serializer_class = serializers.PersonSerializer


class CityView(viewsets.ModelViewSet):

    queryset = City.objects.all()
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