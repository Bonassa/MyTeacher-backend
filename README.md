# Backend projeto MyTeacher

## Stack utilizada
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

## Feramentas utilizadas
- [Django REST](https://www.django-rest-framework.org/#installation)
- [Django CORS Headers](https://pypi.org/project/django-cors-headers/)

## Criação do projeto
- Criar pasta do projeto
- Criar uma virtual env no python, para instalar as dependencias do projeto de maneira local, sem precisar utilizar instalação global, igual seria um projeto com node e npm
```
  python -m venv .venv

  .\.venv\Scripts\activate
```

- Após instalar o Django, para criar o projeto usamos o comando
``` bash-
  django-admin startproject myteacher .
```

- Criação de uma app, uma app é um módulo do meu backend
```
  python .\manage.py startapp teacher
```

## Instalação de bibliotecas
Para instalar as bibliotecas no python é usado o pip, gerenciador de pacotes do python

- Instalação do Django
``` bash
  pip install django
```

- Instalação do Django REST
``` bash
  pip install djangorestframework
```

- Instalação do Django CORS Headers
``` bash
  pip install django-cors-headers
```

- Instalação do Dotenv
```
  pip install python-dotenv
```

## Banco de dados
O Django por padrão usa o banco de dados SQLite3
Para criar e executar uma migration é usado os comandos
```
  python .\manage.py makemigrations
  
  python .\manage.py migrate
```

Para converter o banco de dados em JSON, é utilizado serializers, criando dentro do app um arquivo serializers.py

## Configurando o CORS
CORS (Cross-origin Resource Sharing) é responsável por permitir que o front-end se comunique com o back-end, por padrão é realizado o bloqueio de qualquer requisição que seja feita de uma origin diferente da qual está rodando o servidor

## Instalação do DOTENV
Para proteger as keys do projeto, neste caso apenas a secret key do Django, iremos utilizar variaveis de ambiente.

Como este projeto não está em produção, a SECRET_KEY do Django é

`SECRET_KEY = 'django-insecure-&kr4zww^p3)z$n26#onkqp&pmknn00jrx2*i77$_j2h(r06o6k'`

## Execução do projeto
- Este projeto foi criado utilizando virtualenv para controlar as versões das dependências, caso algum pacote seja adicionado, execute o comando abaixo para atualizar o requirements.txt
``` bash
  pip freeze > requirements.txt
```

- Para instalar as dependências execute os passos abaixo
```
  python -m venv .venv

  .\.venv\Scripts\activate

  pip install -r requirements.txt
```

- Execução do servidor em modo de desenvolvimento
```
  python .\manage.py runserver
```

## Sobre o Django
O Django é um framework python voltado para o desenvolvimento web seguindo o padrão MVT (parecido com o MVC)
- Model (Estrutura dos dados)
- View (Retorno dos dados)
- Templates (Parte visual da aplicação HTML)

Porém para utilizar o Django como apenas um backend, criando as APIs e rotornando não HTML, mas JSON, vamos utilizar o Django REST Framework.