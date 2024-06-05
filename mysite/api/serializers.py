from rest_framework import serializers
from .models import RealEstate

class RealEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = '__all__'

class HomeInputSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    bedrooms = serializers.IntegerField()
    bathrooms = serializers.FloatField()
    sqft_living = serializers.IntegerField()
    sqft_lot = serializers.IntegerField()
    floors = serializers.FloatField()
    waterfront = serializers.BooleanField()
    view = serializers.IntegerField()
    condition = serializers.IntegerField()
    sqft_above = serializers.IntegerField()
    sqft_basement = serializers.IntegerField()
    yr_built = serializers.IntegerField()
    yr_renovated = serializers.IntegerField(allow_null=True, required=False)
    street = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=100)
    statezip = serializers.CharField(max_length=20)
    country = serializers.CharField(max_length=50)