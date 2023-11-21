# serializers.py

from rest_framework import serializers
from apps.dashboard.models import Category, Option, Dataname, DataValue

class DatanameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataname
        fields = '__all__'
