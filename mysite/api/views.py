from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RealEstate
from .serializers import RealEstateSerializer

@api_view(['GET'])
def budget_homes(request):
    min_price = request.query_params.get('min_price', None)
    max_price = request.query_params.get('max_price', None)

    if min_price is None or max_price is None:
        return Response({"error": "Please provide both min_price and max_price"}, status=400)

    try:
        min_price = int(min_price)
        max_price = int(max_price)
    except ValueError:
        return Response({"error": "min_price and max_price must be integers"}, status=400)

    homes = RealEstate.objects.filter(price__gte=min_price, price__lte=max_price)
    serializer = RealEstateSerializer(homes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def homes_by_min_sqft(request):
    min_sqft = request.query_params.get('minsqft', None)

    if min_sqft is None:
        return Response({"error": "Please provide min_sqft"}, status=400)

    try:
        min_sqft = int(min_sqft)
    except ValueError:
        return Response({"error": "min_sqft must be an integer"}, status=400)

    homes = RealEstate.objects.filter(sqft_living__gt=min_sqft)
    serializer = RealEstateSerializer(homes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def homes_by_year(request):
    year = request.query_params.get('year', None)

    if year is None:
        return Response({"error": "Please provide year"}, status=400)

    try:
        year = int(year)
    except ValueError:
        return Response({"error": "year must be an integer"}, status=400)

    homes = RealEstate.objects.filter(models.Q(yr_built__gt=year) | models.Q(yr_renovated__gt=year))
    serializer = RealEstateSerializer(homes, many=True)
    return Response(serializer.data)



