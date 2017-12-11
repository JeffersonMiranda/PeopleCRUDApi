from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from app.models.Address import Address
from app.models.Email import Email
from app.models.PhoneNumber import PhoneNumber
from app.models.Person import Person


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'

class PhoneNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneNumber
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Email
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    
    addresses = AddressSerializer(many=True)
    phoneNumbers = PhoneNumberSerializer(many=True, read_only = True)
    emails = EmailSerializer(many = True, read_only = True)

    class Meta:
        model = Person
        fields = ('firstName','lastName','birthday','addresses','phoneNumbers','emails')


    def create(self, validated_data):
        addresses_data = validated_data.pop('addresses')
        emails_data = validated_data.pop('emails')

        newPerson = Person.objects.create(**validated_data)
        
        for address_data in addresses_data:
            Address.objects.create(person = newPerson, **address_data)
        
        for phoneNumber_data in phoneNumbers_data:
            PhoneNumber.objects.create(person = newPerson, **phoneNumber_data)
        
        for email_data in emails_data:
            Email.objects.create(person = newPerson, **email_data)
        
        return newPerson    

