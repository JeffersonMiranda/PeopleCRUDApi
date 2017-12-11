from rest_framework import serializers
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
    
    addresses = AddressSerializer(many=True,read_only=True)
    phoneNumbers = PhoneNumberSerializer(many=True,read_only=True)
    emails = EmailSerializer(many = True,read_only=True)

    class Meta:
        model = Person
        fields = ('firstName','lastName','birthday','addresses','phoneNumbers','emails')
