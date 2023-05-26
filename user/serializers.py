from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

    def validate(self,attrs):
        from django.contrib.auth.password_validation import validate_password
        from django.contrib.auth.hashers import make_password
        password =attrs['password']
        validate_password(password)
        attrs.update(
            {
                'password':make_password(password)
            }
        )
        return super().validate(attrs)