FROM python:3.11-slim

# Evita que o Python grave arquivos pyc no disco
ENV PYTHONDONTWRITEBYTECODE=1
# Evita que o Python armazene a saída no buffer
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependências do sistema necessárias para compilar pacotes Python
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
