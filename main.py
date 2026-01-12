import logging
from src.database import DBManager
from src.pipeline import EcommerceETL

# Configurazione logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def run_pipeline():
    db = DBManager()
    etl = EcommerceETL(db)
    
    # Percorso del file dati
    data_file = "data/supplier_data.json"
    
    try:
        raw_data = etl.extract(data_file)
        clean_data = etl.transform(raw_data)
        etl.load(clean_data)
        print("\n✅ Pipeline completata con successo!")
    except FileNotFoundError:
        print(f"\n❌ Errore: Assicurati che il file {data_file} esista.")

if __name__ == "__main__":
    run_pipeline()