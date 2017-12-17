from rest_framework import serializers
from app.models.Address import Address
from app.models.Email import Email
from app.models.PhoneNumber import PhoneNumber
from app.models.Person import Person


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': False,'required':False}}

class PhoneNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneNumber
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': False,'required':False}}

class EmailSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Email
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': False,'required':False}}

class PersonSerializer(serializers.ModelSerializer):

    addresses = AddressSerializer(many=True)
    phoneNumbers = PhoneNumberSerializer(many=True)
    emails = EmailSerializer(many = True)

    class Meta:
        model = Person
        fields = ('id','firstName','lastName','birthday','addresses','phoneNumbers','emails')
        extra_kwargs = {'id': {'read_only': False,'required':False}}

    def create(self, validated_data):
        addresses_data = validated_data.pop('addresses')
        phoneNumbers_data = validated_data.pop('phoneNumbers')
        emails_data = validated_data.pop('emails')

        newPerson = Person.objects.create(**validated_data)
        
        for address_data in addresses_data:
            Address.objects.create(person = newPerson, **address_data)
        
        for phoneNumber_data in phoneNumbers_data:
            PhoneNumber.objects.create(person = newPerson, **phoneNumber_data)
        
        for email_data in emails_data:
            Email.objects.create(person = newPerson, **email_data)
        
        return newPerson   

    def update(self,instance,validated_data):
        instance.firstName = validated_data.get('firstName',instance.firstName)
        instance.lastName = validated_data.get('lastName',instance.lastName)
        instance.birthday = validated_data.get('birthday',instance.birthday)
        instance.save()

        addresses_data = validated_data.get('addresses')
        phoneNumbers_data = validated_data.get('phoneNumbers')
        emails_data = validated_data.get('emails')

        ## DELETING OBJECTS
        emails_db_keys = Email.objects.filter(person_id = instance.id).values_list('id', flat=True) ## EMAILS FROM DATABASE        
        emails_keys = list(map(lambda x: x.get('id'), emails_data))    ## EMAILS FROM REQUEST 

        if emails_keys:
            for key in emails_db_keys:
                if key not in emails_keys:
                    Email.objects.filter(id=key).delete()
        else:
            Email.objects.filter(person_id = instance.id).all().delete()

       
        phone_db_keys = PhoneNumber.objects.filter(person_id = instance.id).values_list('id',flat = True)  ## PHONE NUMBERS FROM DATABASE
        phone_keys = list(map(lambda x: x.get('id'), phoneNumbers_data)) ## PHONE NUMBERS FROM REQUEST

        if phone_keys:
            for key in phone_db_keys:
                if key not in phone_keys:
                    PhoneNumber.objects.filter(id=key).delete()
        else:
            PhoneNumber.objects.filter(person_id = instance.id).all().delete()


        address_db_keys = Address.objects.filter(person_id = instance.id).values_list('id',flat = True)  ## ADDRESSES FROM DATABASE
        address_keys = list(map(lambda x: x.get('id'), addresses_data)) ## ADDRESSES FROM REQUEST

        if address_keys:
            for key in address_db_keys:
                if key not in address_keys:
                    Address.objects.filter(id=key).delete()
        else:
            Address.objects.filter(person_id = instance.id).all().delete()



        ## UPDATING OBJECTS    
        if addresses_data:
            for address in addresses_data:
                address_id = address.get('id',None)                
                if address_id:  ## MODIFY ADDRESS IF IT EXISTS
                    addressItem = Address.objects.get(id=address_id, person = instance)
                    addressItem.street = address.get('street', addressItem.street)
                    addressItem.postalCode = address.get('postalCode',addressItem.postalCode)
                    addressItem.city = address.get('city',addressItem.city)
                    addressItem.state = address.get('state',addressItem.state)
                    addressItem.save()
                else:  ## IF ADDRESS DOES NOT EXIST SO CREATE NEW ONE                   
                    Address.objects.create(person_id = instance.id, **address)
        
        if phoneNumbers_data:
            for phoneNumber in phoneNumbers_data:
                phoneNumber_id = phoneNumber.get('id',None)
                if phoneNumber_id:  ## MODIFY PHONE NUMBER IF IT EXISTS
                    phoneNumberItem = PhoneNumber.objects.get(id=phoneNumber_id, person_id = instance)
                    phoneNumberItem.number = phoneNumber.get('number', phoneNumberItem.number)
                    phoneNumberItem.save()
                else:  ## IF ADDRESS DOES NOT EXIST SO CREATE NEW ONE
                    PhoneNumber.objects.create(person_id = instance.id, **phoneNumber)
        
        if emails_data:
            for email in emails_data:
                email_id = email.get('id',None)
                if email_id:  ## MODIFY ADDRESS IF IT EXISTS
                    emailItem = Email.objects.get(id=email_id, person = instance)
                    emailItem.description = email.get('description', emailItem.description)
                    emailItem.save()
                else:  ## IF ADDRESS DOES NOT EXIST SO CREATE NEW ONE
                    Email.objects.create(person_id = instance.id, **email)     


        return instance


        