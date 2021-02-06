# Módulo Bônus - Criando uma interface Web para seus scripts

## Motivos para ter uma interface para seus scripts

- Evitar ter que passar um treinamento para execução dos códigos;
- Criar uma solução mais robusta para nossos clientes;
- Centralizar tipos de script em uma interface web.

## Etapas de aprendizado

AULA 01 
- Conhecendo o conceito básico do django
- Instalar o django
- Criar o primeiro **projeto**
- Conhecendo as caracteristicas do projeto
- Conhecendo o settings.py
- Iniciar o servidor DJANGO
- Conhecendo o ciclo de requisição do DJANGO

AULA 02
- Conhecendo e criar uma **aplicacao**
- Conhecendo makemigrations e migrate
- Criando nosso primeiro MODEL
  - Criar o model no arquivo .models
- Conhecendo o DJANGO ADMIN
  - Registrar as aplicações
    -  Adicionar o models no admin.py para aparecer no DJANGO ADMIN

AULA 03
- CONHECER O QUE É CRUD
  - C -> create
  - R -> read
  - U -> update
  - D -> delete
- CRIAR UM CRUD
  - CRIAR CREATE
  - CRIAR READ

AULA 04 
- CRIAR UPDATE
- CRIAR DELETE

AULA 05
- CRIANDO TEMPLATE BASE
- TRABALHANDO COM BOOTSTRAP

AULA 06
- CONTINUACAO BOOTSTRAP
- ENTENDENDO O JINJA 2

AULA 07
- COMO UTILIZAR BANCO DE DADOS POSTGRESQL

AULA 08 
- EXECUTANDO UM SCRIPT PELA INTERFACE WEB



### Criar o primeiro projeto

```
django-admin startproject pastelariaDevops .
```

### Caracteristicas do projeto

```
.
├── README.md
├── manage.py - Utilitário de linha de comando para tarefas administrativas
└── pastelariaDevops - Pasta do nosso projeto
    ├── __init__.py
    ├── asgi.py
    ├── settings.py - Arquivo mais importante do projeto, toda configuração relacionado ao projeto será feita nesse arquivo
    ├── urls.py - URLS do projeto
    └── wsgi.py - Entrypoint da aplicação, utilizado para trabalhar com servidores Web.
```


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

### CRIAR UM CRUD COMPLETO

#### CREATE 

Na URL do projeto, apontar para a URL da aplicação

```
from pastelariaDevops.core import urls as core_url
```

Add a ultima linha que mostra o include

```
urlpatterns = [
    path('healthcheck', healthcheck),
    path('mymachine', mymachine),
    path('hello', hello),
    path('admin/', admin.site.urls),
    path('loja/', include(core_url))
]
```

Criar um formulário

Dentro da app criar o arquivo **forms.py**

```
from django import forms
from django.forms import ModelForm
from .models import Loja

class LojaForm(ModelForm):
    class Meta:
        model = Loja
        fields = '__all__'
```

Na view da app

```
from django.shortcuts import render
from .models import Loja
from .forms import LojaForm

# Create your views here.

def create_loja(request):
    form = LojaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('loja_obrigado')
    return render(request, 'loja_form.html', {"form": form})
```

Criar a pasta **templates** dentro da app

Criar o arquivo **loja_form.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário LOJA</title>
</head>
<body>

    <form action="" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form }}
        <button type="submit">Salvar</button>
    </form>
    
</body>
</html>
```

#### READ

Na URL da app, criar uma nova URL para lista de lojas.

Nas views

```
def read_loja(request):
    lojas = Loja.objects.all()
    return render(request, 'loja_lista.html', {"lojas": lojas})
```

Cria o arquivo **loja_lista.html**

`Usar o modelo de tabela do site bootstrap como referência`

Edit no views de create para redirecionar para a pagina de lista de lojas, após criar uma nova loja.

#### UPDATE

Criar uma view (na aplicacao) que faz a busca do objeto por ID no banco de dados

```
def update_loja(request, id):
    loja = get_object_or_404(Loja, pk=id)
    print(loja)
    form = LojaForm(request.POST or None, request.FILES or None, instance=loja)
    print(form)

    if form.is_valid():
        form.save()
        return redirect('read_loja')
    return render(request, 'loja_form.html', {"form": form})
```

Criar a URL no app

```
from .views import update_loja

urlpatterns = [
    path('', create_loja, name='create_loja'),
    path('lista', read_loja, name='read_loja'),
    path('update/<int:id>', update_loja, name='update_loja')
]
```

No formulário que lista os objetos (html de lista)
Adicionar um link para a URL de update, passando a instante de id do objeto

```
        <tbody>
          {% if lojas %}
          {% for loja in lojas %}
          <tr>
            <th><a href="{% url 'update_loja' loja.id %}">{{ loja.id }}</a></th>
            <td>{{ loja.name }}</td>
            <td>{{ loja.endereco }}</td>
            <td>{{ loja.status }}</td>
          </tr>
          {% endfor %}
          {% endif %}
        </tbody>
    </table>
```

#### DELETE 

Criar a view para deletar o objeto do banco de dados

```
def delete_loja(request, id):
    loja = get_object_or_404(Loja, pk=id)
    form = LojaForm(request.POST or None, request.FILES or None, instance=loja)
    if request.method == 'POST':
        loja.delete()
        return redirect('read_loja')
    return render(request, 'loja_delete_confirm.html', {'form': form, 'loja': loja})
```

Criar a pagina de confirmação de delete

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário LOJA</title>
</head>
<body>

    <h1>Tem certeza que deseja delete {{ loja }}</h1>
    <form action="" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form }}
        <button type="submit">Delete</button>
    </form>
    
</body>
</html>
```

Criar URL na app para delete

```
from .views import delete_loja

urlpatterns = [
    path('', create_loja, name='create_loja'),
    path('lista', read_loja, name='read_loja'),
    path('update/<int:id>', update_loja, name='update_loja'),
    path('delete/<int:id>', delete_loja, name='delete_loja')
]
```

No template de HTML que lista os objetos, adicionar o link para URL de delete

```
        <tbody>
          {% if lojas %}
          {% for loja in lojas %}
          <tr>
            <th><a href="{% url 'update_loja' loja.id %}">{{ loja.id }}</a></th>
            <td>{{ loja.name }}</td>
            <td>{{ loja.endereco }}</td>
            <td>{{ loja.status }}</td>
            <td><a href={% url 'delete_loja' loja.id %}>Delete</a></td>
          </tr>
          {% endfor %}
          {% endif %}
        </tbody>
    </table>
```


## TRABALHANDO COM TEMPLATE BASE

1. Criar um arquivo HTML para a nossa BASE.

```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>

<h1>Esse arquivo esta carregando o template base</h1>

{% block main %}
{% endblock %}
    
</body>
</html>
```

2. Carregar o template BASE nas outras PÁGINAS HTML

```
{% extends 'base.html' %}

{% block title %}
Formulário nova loja
{% endblock %}

{% block main %}

    <form action="" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form }}
        <button type="submit">Salvar</button>
    </form>
    
    <a href={% url 'read_loja' %}>Lista de lojas</a>
    
{% endblock %}
```

## Trabalhando com bootstrap

### Adicionando bootstrap no formulário

**Documentação:** https://django-bootstrap-form.readthedocs.io/en/latest/

- Instalar o bootstrap

```
python3 -m pip install django-bootstrap-form
```

- Adicionar o app no settings

INSTALLED_APPS = [
    ...
    'bootstrapform',
    ...
]


- Carrega o bootstrap nos templates de formulário

```
{% extends 'base.html' %}

{% load bootstrap %}

...
```

- Carregar o bootstrp no form

```
    <form action="" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form|bootstrap}}
        <button type="submit">Salvar</button>
    </form>
```

### Deixando o projeto bonito com bootstrap