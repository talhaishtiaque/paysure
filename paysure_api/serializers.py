from .models import Policy, Payment
from rest_framework import serializers


class PolicySerializer(serializers.Serializer):
    external_user_id = serializers.CharField()
    benefit = serializers.CharField()
    currency = serializers.CharField()
    total_max_amount = serializers.IntegerField()

    def create(self, validated_data):
        return Policy.objects.create(**validated_data)

class PaymentSerializer(serializers.Serializer):
    external_user_id = serializers.CharField()
    benefit = serializers.CharField()
    currency = serializers.CharField()
    amount = serializers.IntegerField()
    authorized = serializers.BooleanField()
    reason = serializers.CharField()
    timestamp = serializers.DateTimeField()

    def create(self, validated_data):
        return Payment.objects.create(**validated_data)
