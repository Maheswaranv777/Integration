from rest_framework import serializers
from .models import mars


class marsSerializer(serializers.ModelSerializer):
    class Meta:
        model=mars
        fields='__all__'