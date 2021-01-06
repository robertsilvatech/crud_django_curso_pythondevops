# Módulo Bônus - Criando uma interface Web para seus scripts

## Motivos para ter uma interface para seus scripts

- Evitar ter que passar um treinamento para execução dos códigos;
- Criar uma solução mais robusta para nossos clientes;
- Centralizar tipos de script em uma interface web.

## Etapas de aprendizado

- Conhecendo o conceito básico do django
- Instalar o django
- Criar o primeiro **projeto**
- Conhecendo as caracteristicas do projeto
- Conhecendo o settings.py
- Iniciar o servidor DJANGO
- Conhecendo o ciclo de requisição do DJANGO
- Conhecendo e criar uma **aplicacao**
- Conhecendo makemigrations e migrate
- Criando nosso primeiro MODEL
  - Criar o model no arquivo .models
- Conhecendo o DJANGO ADMIN
  - Registrar as aplicações
    -  Adicionar o models no admin.py para aparecer no DJANGO ADMIN
PROXIMA AULA
- CONHECER O QUE É CRUD
- CRIAR UM CRUD COMPLETO

### Criar o primeiro projeto

```
django-admin startproject pastelariaDevops .
```

### Caracteristicas do projeto
.
├── README.md
├── manage.py - Utilitário de linha de comando para tarefas administrativas
└── pastelariaDevops - Pasta do nosso projeto
    ├── __init__.py
    ├── asgi.py
    ├── settings.py - Arquivo mais importante do projeto, toda configuração relacionado ao projeto será feita nesse arquivo
    ├── urls.py - URLS do projeto
    └── wsgi.py - Entrypoint da aplicação, utilizado para trabalhar com servidores Web.

### settings.py

SECRET_KEY -> Utilizada para efetuar a criptografia das senhas
DEBUG -> Modo de DEBUG, em produção mudar para False
ALLOWED_HOSTS -> Lista de endereços/dominios que serão permitidos acessar o DJANGO
INSTALLED_APPS -> Aplicações instaladas por padrão, aplicações externa instalada ou aplicações que criamos, sempre deve adicionar aqui.
MIDDLEWARE -> Segurança, o DJANGO por padrão ele cuida da parte de segurança
ROOT_URLCONF -> URLS principais do projeto
TEMPLATES -> Responsável por renderizar as paginas HTML. Por padrão considera a pasta template de cada aplicação
WSGI_APPLICATION -> Aplicação do servidor WEB
DATABASES -> Configuração do banco de dados que será utilizado
AUTH_PASSWORD_VALIDATORS -> Validações do padrão de senhas
LANGUAGE_CODE -> Idioma padrão do projeto, utilizaremos em pt-br
TIME_ZONE -> Timezone, no nosso caso utilizar America/Sao_Paulo
STATIC_URL -> Pasta base dos arquivos estaticos

### Iniciar o servidor DJANGO

```
python3 manage.py runserver
```

### Criando a primeira aplicação

```
python3 manage.py startapp pastelaria
```

### makemigrations e migrate

makemigrations - Prepara as alterações que devem ser aplicadas no banco de dados
migrate - Aplica as alterações no banco de dados

```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Criando nosso primeiro MODEL

```
class Lojas(models.Model):
    name = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
        
    #def __str__(self):
    #    return self.name
```

### Criando usuário superadmin Django

```
python3 manage.py createsuperuser
```

### Registrar o model no django admin

No arquivo admin.py da app

```
from django.contrib import admin
from .models import Lojas

# Register your models here.

admin.site.register(Lojas)
```


