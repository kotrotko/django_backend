from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'phone_number',
            'password',
            'date_of_birth',
        ]
