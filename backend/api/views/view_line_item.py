from rest_framework import generics

from api import serializers, models


class LineItemListCreateView(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = serializers.LineItemSerializer
    queryset = models.LineItem.objects.all()


class LineItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = serializers.LineItemSerializer
    queryset = models.LineItem.objects.all()
