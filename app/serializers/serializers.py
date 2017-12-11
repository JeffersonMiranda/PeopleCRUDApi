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

    class Meta:
        model = Person
        fields = ('firstName','lastName','birthday','addresses')

    def create(self, validated_data):
        addresses_data = validated_data.pop('addresses')
        newPerson = Person.objects.create(**validated_data)
        for address_data in addresses_data:
            Address.objects.create(person = newPerson, **address_data)
        return newPerson    

