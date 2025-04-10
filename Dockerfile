# Usa uma imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia os demais arquivos da aplicação
COPY . .

# Expõe a porta usada pela aplicação Flask
EXPOSE 8080

# Define o comando para rodar a aplicação
CMD ["python", "app.py"]
