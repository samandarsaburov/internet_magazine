from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','password','roles')
        
    def create(self,validated_date):
        user = CustomUser(
            username = validated_date['username'],
            roles = validated_date.get('roles',1)
        )
        user.set_password(validated_date['password'])
        user.save()
        return user