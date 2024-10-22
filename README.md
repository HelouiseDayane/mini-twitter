# Mini Twitter

Mini Twitter é uma aplicação de microblogging que permite que usuários postem mensagens, sigam uns aos outros e recebam notificações sobre as atividades de seus seguidores. Esta aplicação foi construída utilizando Python e Django REST framework, com autenticação JWT, documentação Swagger, testes automatizados, banco de dados PostgreSQL, Docker, e implantada no Heroku com integração contínua e entrega contínua (CI/CD).

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal da aplicação.
- **Django REST Framework**: Para construir APIs robustas e escaláveis.
- **JWT (JSON Web Tokens)**: Para autenticação segura de usuários.
- **Swagger**: Para gerar a documentação da API automaticamente.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional utilizado para armazenar dados.
- **Docker**: Para criar contêineres e facilitar o desenvolvimento e a implantação.
- **Heroku**: Plataforma de nuvem para implantação e escalabilidade.
- **CI/CD**: Integração contínua e entrega contínua configuradas para automatizar testes e deploy.

## Diagrama de Arquitetura e ERD

### Diagrama de Entidade-Relacionamento (ERD)

![ERD]([link_para_meu_diagrama_erd.png](https://lucid.app/lucidspark/a0070528-bf0c-4b6e-8697-0097e83ca577/edit?invitationId=inv_3e58e1b9-646b-4e86-9924-c5316254269a))

### Diagrama de Arquitetura

![Diagrama de Arquitetura](link_para_seu_diagrama_de_arquitetura.png)

## Configuração do Ambiente

## Pré-requisitos

- Python 3.8 ou superior
- Docker e Docker Compose
- Conta no Heroku

## Configuração do Projeto

### Passo 1: Clone o Repositório

```bash
git clone https://github.com/helouisedayane/mini-twitter.git
cd mini-twitter

```

### Passo 2: Crie um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # No Windows, use venv\Scripts\activate

```

### Passo 3: Instale as Dependências
```bash
pip install -r requirements.txt
```
### Passo 4: Configurar o Banco de Dados
- **Certifique-se** de que você tenha o PostgreSQL em execução.
- **Crie um banco** de dados chamado mini_twitter_db.
  
### Passo 5: Configurar Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis:
```bash
DATABASE_URL=postgres://postgres:postgres@db:5432/mini_twitter_db
SECRET_KEY=postgres

```

### Passo 6: Executar o Docker Compose
Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis:
```bash
docker-compose up --build
```

### Executar a Aplicação
Acesse a aplicação no navegador em http://localhost:8080/.

### Executar Testes
Para executar os testes da aplicação, utilize o seguinte comando:
```bash
pytest --cov=posts --cov=posts
```

ou

```bash
pytest --cov=posts --cov=users
```


ou 

```bash
docker-compose exec web python manage.py test posts
```
ou

```bash
 docker-compose exec web python manage.py test users
```

### Documentação da API
A documentação da API está disponível no Swagger. Acesse a URL:

```bash
http://localhost:8080/swagger/

```

### Implantação no Heroku
Para implantar a aplicação no Heroku, execute os seguintes comandos:

```bash
heroku login
heroku create mini-twitter
git push heroku main
```

### Configuração de Variáveis de Ambiente
As variáveis de ambiente devem ser configuradas no painel do Heroku ou através do CLI:

```bash
heroku config:set SECRET_KEY='sua_chave_secreta'
heroku config:set DATABASE_URL='postgres://usuario:senha@host:port/dbname'
heroku config:set REDIS_URL='redis://url_do_redis'
```









