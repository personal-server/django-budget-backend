from knox.auth import TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api import serializers, models


class LineItemListCreateView(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = serializers.LineItemSerializer
    queryset = models.LineItem.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class LineItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = serializers.LineItemSerializer
    queryset = models.LineItem.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
