from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

