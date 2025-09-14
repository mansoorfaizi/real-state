from rest_framework import serializers
from api.models.office import Office

class OfficeSerializer(serializers.ModelSerializer):
    property_name = serializers.SerializerMethodField()
    number_of_rooms_display = serializers.SerializerMethodField()
    toilet_display = serializers.SerializerMethodField()
    class Meta:
        model = Office
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
    # Serializer methods
    def get_number_of_rooms_display(self, obj):
        return f"{obj.number_of_rooms} room(s)" if obj.number_of_rooms else "No rooms"

    def get_property_name(self, obj):
        return obj.property.title if obj.property else None

    def get_toilet_display(self, obj):
        return obj.get_toilet_display() if obj.toilet else None

    # validation for number_of_rooms
    def validate_number_of_rooms(self, value):

        if value < 1:
            raise serializers.ValidationError("Number of rooms must be at least 1.")
        return value