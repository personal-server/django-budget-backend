from knox.auth import TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api import serializers, models


class BudgetListCreateView(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = serializers.BudgetSerializer
    queryset = models.Budget.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class BudgetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = serializers.BudgetSerializer
    queryset = models.Budget.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

