from rest_framework import serializers
from .models.house import House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

    # Extra validation for numeric fields
    def validate_bedrooms(self, value):
        if value < 0:
            raise serializers.ValidationError("Bedrooms cannot be negative.")
        return value

    def validate_bathrooms(self, value):
        if value < 0:
            raise serializers.ValidationError("Bathrooms cannot be negative.")
        return value

    def validate_area(self, value):
        if value <= 0:
            raise serializers.ValidationError("Area must be greater than 0.")
        return value

    def validate_floors(self, value):
        if value < 1:
            raise serializers.ValidationError("There must be at least 1 floor.")
        return value
