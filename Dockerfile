# Usa un'immagine leggera di Python
FROM python:3.9-slim

# Imposta la directory di lavoro nel container
WORKDIR /app

# Copia i file dei requisiti 
COPY requirements.txt .

# Installa le dipendenze 
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice nella cartella /app del container
COPY . .

# Comando per avviare la pipeline quando il container parte
CMD ["python", "main.py"]