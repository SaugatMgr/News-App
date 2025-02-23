from rest_framework import serializers


class NewsSerializer(serializers.Serializer):
    country = serializers.CharField(max_length=64, required=True)
    category = serializers.CharField(max_length=64, required=True)
