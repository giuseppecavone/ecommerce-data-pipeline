class EcommerceError(Exception):
    """Classe base per le eccezioni del progetto"""
    def __init__(self, message, status_code=500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class ValidationError(EcommerceError):
    def __init__(self, message):
        super().__init__(message, status_code=400)

class ResourceNotFoundError(EcommerceError):
    def __init__(self, message):
        super().__init__(message, status_code=404)