from rest_framework import serializers

from api import models


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = (
            'id',
            'amount',
            'type',
            'line_item',
            'date'
        )
