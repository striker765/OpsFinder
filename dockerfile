FROM python:3.12

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Use uma imagem base do Python
FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Copie o arquivo de dependências e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código do projeto
COPY . .

# Define a variável de ambiente para o Django
ENV DJANGO_SETTINGS_MODULE=seu_projeto.settings

# Exponha a porta que será usada pelo contêiner
EXPOSE 8000

# Comando para rodar o servidor Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "seu_projeto.wsgi:application"]
