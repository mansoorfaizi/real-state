from rest_framework import serializers
from api.models.district import District

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__' 
