# 1. Temel imaj olarak resmi Python 3.10 slim versiyonunu kullan
FROM python:3.10-slim

# 2. Çalışma dizinini /app olarak ayarla
WORKDIR /app

# 3. Logların ve çıktıların doğrudan görünmesi için ayarlar
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# 4. Önce sadece gereksinimler dosyasını kopyala ve kur
#    Bu sayede, kod değiştiğinde kütüphaneler tekrar kurulmaz (Docker cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Projenin geri kalan tüm dosyalarını kopyala
#    (app.py, static/, templates/, trained_models/ vb.)
COPY . .

# 6. Uygulamayı çalıştıracak komut
#    Railway, $PORT adında bir ortam değişkeni sağlar.
#    Gunicorn'a 0.0.0.0 adresinden bu PORT'u dinlemesini söylüyoruz.
#    'app:app', app.py dosyasındaki 'app' isimli Flask objesini hedefler.
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]