from rest_framework import serializers
from .models import KYCForm

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()

class KYCFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYCForm
        fields = '__all__'

    def validate_aadhar_number(self, value):
        if not len(value) == 12:
            raise serializers.ValidationError("Aadhar number must be exactly 12 digits.")
        try:
            aadhar_number = int(value)
        except:
            raise serializers.ValidationError("Aadhar number must be Number")
        return value

    def validate_email(self, value):
        if not value.endswith("@gmail.com"):
            raise serializers.ValidationError("Only Gmail addresses are allowed.")
        return value

    def validate(self, data):
        if data['aadhar_front'] == data['aadhar_back']:
            raise serializers.ValidationError("Aadhar front and back files must be different.")
        return data
