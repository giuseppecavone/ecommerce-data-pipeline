import logging
from functools import wraps

def log_execution(func):
    """Decoratore per monitorare l'inizio e la fine dei processi ETL"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f">>> Avvio fase: {func.__name__.upper()}")
        result = func(*args, **kwargs)
        logging.info(f"<<< Completata fase: {func.__name__.upper()}")
        return result
    return wrapper