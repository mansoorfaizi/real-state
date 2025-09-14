from rest_framework import serializers
from api.models.property import Property, PropertyMedia


class PropertyMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyMedia
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField()
    deal_type_display = serializers.SerializerMethodField()
    property_type_display = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    # Serializer methods
    def get_media(self, object):
        media = PropertyMedia.objects.filter(property=object)
        return PropertyMediaSerializer(media, many=True).data

    def get_deal_type_display(self, object):
        return object.get_deal_type_display()

    def get_property_type_display(self, object):
        return object.get_property_type_display()
