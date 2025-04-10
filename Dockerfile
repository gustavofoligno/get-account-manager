FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependência e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto dos arquivos da aplicação
COPY . .

# Expõe a porta (caso seu app use alguma, como Flask)
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
