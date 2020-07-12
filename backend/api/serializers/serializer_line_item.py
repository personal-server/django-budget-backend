from rest_framework import serializers

from api import models


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LineItem
        fields = (
            'id',
            'amount',
            'type',
            'budget'
        )
