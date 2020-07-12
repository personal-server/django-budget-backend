from rest_framework import generics

from api import serializers, models


class BudgetListCreateView(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = serializers.BudgetSerializer
    queryset = models.Budget.objects.all()


class BudgetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = serializers.BudgetSerializer
    queryset = models.Budget.objects.all()
