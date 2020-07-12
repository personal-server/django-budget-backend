from rest_framework import serializers

from api import models


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Budget
        fields = (
            'id',
            'start_date',
            'end_date'
        )
