from rest_framework import generics

from api import serializers, models


class TransactionListCreateView(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = serializers.TransactionSerializer
    queryset = models.Transaction.objects.all()


class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = serializers.TransactionSerializer
    queryset = models.Transaction.objects.all()
