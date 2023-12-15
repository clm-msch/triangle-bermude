from rest_framework import serializers

from .models import Event, Occurrence, Price_type, Access_type, Group, Adresse, Audience, Tag


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        
class OccurenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = "__all__"

class Price_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price_type
        fields = "__all__"

class Access_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access_type
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class AdresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields = "__all__"

class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"