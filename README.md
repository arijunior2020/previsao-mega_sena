# Previsão Mega-Sena
Este projeto tem como objetivo prever os números da Mega-Sena utilizando técnicas de aprendizado de máquina e análise de dados.

## Estrutura do Projeto

- `static/`: Contém arquivos CSS e outros arquivos estáticos.
- `templates/`: Contém os arquivos HTML.
- Arquivos Python na raiz do projeto para processamento de dados e treinamento de modelos.

## Requisitos

- Python 3.8+
- Flask
- Pandas
- NumPy
- Matplotlib
- Bibliotecas listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/arimateiajunior/previsao-mega_sena.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd previsao-mega_sena
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Execute o script de processamento de dados:
    ```bash
    python process_data.py
    ```
2. Treine o modelo:
    ```bash
    python train_model.py
    ```
3. Inicie a aplicação Flask:
    ```bash
    flask run
    ```
4. Acesse a aplicação web em `http://127.0.0.1:5000` para fazer previsões.


## Docker

### Usando Docker

### Dockerfile

Certifique-se de que você tem um arquivo `Dockerfile` na raiz do projeto com o seguinte conteúdo:

```Dockerfile
# Use uma imagem base do Python
FROM python:3.8-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Exponha a porta que a aplicação irá rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
```

### docker-compose.yml

Certifique-se de que você tem um arquivo `docker-compose.yml` na raiz do projeto com o seguinte conteúdo:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    environment:
      - FLASK_ENV=development
```
1. Construa a imagem Docker:
    ```bash
    docker build -t previsao-mega_sena .
    ```
2. Inicie os containers com Docker Compose:
    ```bash
    docker-compose up
    ```
3. Acesse a aplicação web em `http://127.0.0.1:5000` para fazer previsões.