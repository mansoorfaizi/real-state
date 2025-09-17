from rest_framework import serializers
from api.models.house import House
from api.models.property import Property


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"  # include all model fields automatically

    # --- Numeric Validations ---
    def validate_bedrooms(self, value):
        if value < 0:
            raise serializers.ValidationError("Bedrooms must be 0 or greater.")
        return value

    def validate_bathrooms(self, value):
        if value < 0:
            raise serializers.ValidationError("Bathrooms must be 0 or greater.")
        return value

    def validate_total_area_m2(self, value):
        if value < 0:
            raise serializers.ValidationError("Total area must be 0 or greater.")
        return value

    def validate_built_area_m2(self, value):
        if value < 0:
            raise serializers.ValidationError("Built area must be 0 or greater.")
        return value

    def validate_floors_no(self, value):
        if value < 0:
            raise serializers.ValidationError("Floors number must be 0 or greater.")
        return value

    # --- Choice Field Validation ---
    def validate_water_type(self, value):
        valid_choices = [choice[0] for choice in House.WATER_CHOICES]
        if value not in valid_choices:
            raise serializers.ValidationError(f"Water type must be one of: {', '.join(valid_choices)}")
        return value

    # --- Foreign Key Validation (property) ---
    def validate_property(self, value):
        if value and not Property.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Invalid property selected.")
        return value