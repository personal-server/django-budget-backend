from rest_framework import serializers

from api import models


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = models.Transaction
        fields = '__all__'
