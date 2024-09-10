from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'linked_user']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            linked_user=validated_data['linked_user']
        )
        
        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Adicione o ID do usuário ao token
        token['user_id'] = user.id

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        
        user = self.user
        
        data['user_id'] = user.id
        
        return data
