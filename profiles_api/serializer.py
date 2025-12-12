from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer a name field testing for out ApiView"""
    name=serializers.CharField(max_length=10)
    