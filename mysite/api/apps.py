from django.apps import AppConfig
import os

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from .utils import load_csv_data
        csv_file_path = "/workspaces/Django-test/data0967ed6.csv"
        if os.path.exists(csv_file_path):
            print("Loading data from CSV file")
            load_csv_data(csv_file_path)
        else:
            print("CSV file does not exist")
