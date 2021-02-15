from rest_framework import serializers
from quickstart.models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead 
        fields = '__all__'

