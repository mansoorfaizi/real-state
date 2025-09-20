from rest_framework import serializers
from api.models.office import Office

class OfficeSerializer(serializers.ModelSerializer):
    property_name = serializers.SerializerMethodField()
    class Meta:
        model = Office
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
    # Serializer methods

    def get_property_name(self, object):
        return object.property.title if object.property else None

    # validation for number_of_rooms
    def validate_number_of_rooms(self, value):

        if value < 1:
            raise serializers.ValidationError("Number of rooms must be at least 1.")
        return value