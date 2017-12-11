from django.shortcuts import render
from django.db import transaction
from django.db.utils import IntegrityError
from app.models.Address import Address
from app.models.Email import Email
from app.serializers import serializers
from app.models.PhoneNumber import PhoneNumber
from app.models.Person import Person
from rest_framework import viewsets
from datetime import datetime

class PersonView(viewsets.ModelViewSet):

    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer

    def create(self,request,*args,**kwargs):
        dataPerson = request.data['data']
        dataAddress = request.data['address']
        dataEmail = request.data['email']
        dataPhoneNumber = request.data['phoneNumber']

        serializerPerson = serializers.PersonSerializer(data=dataPerson)        
        serializerPerson.is_valid(raise_exception=True) # VALIDANDO O SERIALIZER

        try:
            with transaction.atomic():
                self.perform_create(serializerPerson)
                
                for address in dataAddress:
                    address['person'] = 1

                serializerAddress = serializers.AddressSerializer(data = dataAddress,many = isinstance(dataAddress,list))
                serializerAddress.is_valid(raise_exception=True) 
                Address = AddressView()
                Address.perform_create(serializerAddress)
                
                for email in dataEmail:
                    email['person'] = serializerPerson.data['id']

                serializerEmail = serializers.EmailSerializer(data = dataEmail,many=isinstance(dataEmail,list))
                serializerEmail.is_valid(raise_exception = True)
                Email = EmailView()
                Email.perform_create(serializerEmail)

                for phoneNumber in dataPhoneNumber:
                    phoneNumber['person'] = serializerPerson.data['id']
    
                serializerPhoneNumber = serializers.PhoneNumberSerializer(data = dataPhoneNumber,many=isinstance(dataPhoneNumber,list))
                serializerPhoneNumber.is_valid(raise_exception = True)
                PhoneNumber = PhoneNumberView()
                PhoneNumber.perform_create(serializerPhoneNumber)
                
        except IntegrityError:
             handle_exception()
                
    
class AddressView(viewsets.ModelViewSet):

    queryset = Address.objects.all()
    serializer_class = serializers.AddressSerializer

class PhoneNumberView(viewsets.ModelViewSet):

    queryset = PhoneNumber.objects.all()
    serializer_class = serializers.PhoneNumberSerializer

class EmailView(viewsets.ModelViewSet):

    queryset = Email.objects.all()
    serializer_class = serializers.EmailSerializer