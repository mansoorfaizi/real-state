from rest_framework import serializers
from api.models.currency import Currency   

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name', 'symbol', 'created_at', 'updated_at']
