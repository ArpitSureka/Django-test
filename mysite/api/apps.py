from django.apps import AppConfig
import os

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from .utils import load_csv_data
        csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'realestate_data.csv')
        if os.path.exists(csv_file_path):
            load_csv_data(csv_file_path)
