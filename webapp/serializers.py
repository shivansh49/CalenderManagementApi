from rest_framework import serializers
from .models import usrs,Event
class usrsSerializer(serializers.ModelSerializer):
    class Meta:
        model = usrs
        fields = ['Name','Email']
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id','Email','Date','Title','Description']

