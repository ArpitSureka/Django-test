import csv
from datetime import datetime
from .models import RealEstate

def load_csv_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            real_estate = RealEstate(
                date=datetime.strptime(row['date'], '%m-%d-%Y %H:%M'),
                price=int(row['price']),
                bedrooms=int(row['bedrooms']),
                bathrooms=float(row['bathrooms']),
                sqft_living=int(row['sqft_living']),
                sqft_lot=int(row['sqft_lot']),
                floors=float(row['floors']),
                waterfront=bool(int(row['waterfront'])),
                view=int(row['view']),
                condition=int(row['condition']),
                sqft_above=int(row['sqft_above']),
                sqft_basement=int(row['sqft_basement']),
                yr_built=int(row['yr_built']),
                yr_renovated=int(row['yr_renovated']) if row['yr_renovated'] else None,
                street=row['street'],
                city=row['city'],
                statezip=row['statezip'],
                country=row['country']
            )
            real_estate.save()
