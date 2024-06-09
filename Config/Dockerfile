# Gunakan image dasar yang berisi Python
FROM python:3.11-slim

RUN apt-get update && apt-get install build-essential -y
RUN apt-get install -y curl wget git

# Set lingkungan kerja di dalam container
WORKDIR /app

# Salin seluruh kode aplikasi ke dalam container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Tentukan port yang digunakan oleh Streamlit
EXPOSE 8080

# Jalankan aplikasi Streamlit
ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=8080", "--server.address=0.0.0.0"]
