from knox.auth import TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api import serializers, models


class TransactionListCreateView(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = serializers.TransactionSerializer
    queryset = models.Transaction.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = serializers.TransactionSerializer
    queryset = models.Transaction.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
