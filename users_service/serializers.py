from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=5, style={"input_type": "password"})

    class Meta:
        model = get_user_model()
        fields = ("id", "email", "first_name", "last_name", "password", "is_staff")
        read_only_fields = ("is_staff",)

    def create(self, validated_data):
        """Create a new users_service with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a users_service, set the password correctly and return it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user
