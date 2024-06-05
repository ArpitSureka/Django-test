from django.urls import path
from .views import *

urlpatterns = [
    path('budget-homes/', budget_homes, name='budget-homes'),
    path('homes-by-min-sqft/', homes_by_min_sqft, name='homes-by-min-sqft'),
]
