from rest_framework import serializers
from .models import Moviedata

# creating a serializer
class MoviedataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moviedata
        fields = ['id','name','duration','rating']

