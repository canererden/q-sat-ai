# Python 3.11 tabanlı minimal imaj
FROM python:3.11-slim

# Çalışma dizini
WORKDIR /app

# Gereksinimleri yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Tüm dosyaları kopyala
COPY . .

# Railway Flask uygulamaları için PORT değişkeni kullanır
ENV PORT=5000

# Flask uygulamasını başlat
CMD ["python", "app.py"]