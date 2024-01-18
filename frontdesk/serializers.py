from rest_framework import serializers
from .models import GuestInfo, GuestRoom

class GuestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestInfo
        field = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestRoom
        fields = '__all__'