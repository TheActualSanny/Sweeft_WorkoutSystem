''' The serializers that will be used during Django user authentication will be written here. '''
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserRegisterSerializer(serializers.ModelSerializer):
    '''
        Instance of this serializer class will be used whenever the user registers
        a new account, the main purpose of this class is to serve as a validator.
    '''
    password_confirm = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']
        extra_kwargs = {
            'password' : {'write_only' : True, 'min_length' : 4},
            'password_confirm' : {'write_only' : True}
        }

    def validate(self, data):
        '''
            We override this in order to check that password_confirm 
            is equal to password.
        '''
        if not data['password'] == data['password_confirm']:
            raise serializers.ValidationError('Make sure that you input the same password twice!')
        return data
    
    # def create(self, validated_data):
        '''
            In order to write the password in a saved state, we override the
            create() method.
            The implementation will be written here, for now the password will be stored as a string
        '''



