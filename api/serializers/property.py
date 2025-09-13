
from rest_framework import serializers
from api.models.property import Property, PropertyMedia

class PropertyMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyMedia
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    media = PropertyMediaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Property
        fields = '__all__'
