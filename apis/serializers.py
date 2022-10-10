from rest_framework import serializers
from apis.models import LeadModel

class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeadModel
        fields = '__all__'