import json
from .decorators import log_execution

class EcommerceETL:
    def __init__(self, db_manager):
        self.db = db_manager

    @log_execution
    def extract(self, file_path):
        with open(file_path, 'r') as f:
            return json.load(f)

    @log_execution
    def transform(self, raw_data):
        # Data Cleaning: filtriamo prezzi negativi o dati mancanti
        cleaned_data = []
        for item in raw_data:
            if item.get('price', 0) > 0 and item.get('name'):
                cleaned_data.append(item)
        return cleaned_data

    @log_execution
    def load(self, cleaned_data):
        for item in cleaned_data:
            self.db.insert_product(item['name'], item['price'], item.get('category', 'N/A'))