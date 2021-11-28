
# WEB application to register users #

# Aplicação WEB para cadastro de usuario #

______________________________________________________________________________________________________________________________________________________________________________________

# First step #

Instantiate Postgres server with the docker command below:

'docker run --name darth-vader-postgres -p 5432:5432 -e POSTGRES_PASSWORD='postgres' -d postgres:10-alpine'

To stop the postgres docker use the command below:

'docker stop $(docker ps -aq); docker rm $(docker ps -aq)'

# Primeiro passo #

Instanciar o Postgres via comando docker abaixo:

'docker run --name darth-vader-postgres -p 5432:5432 -e POSTGRES_PASSWORD='postgres' -d postgres:10-alpine'

Para parar a docker utilizar o comando abaixo:

'docker stop $(docker ps -aq); docker rm $(docker ps -aq)'

_________________________________________________________________________________________________________________________________________________________________________________

# Second step #

Instantiate the python virtual machine with the command below:

'python -m venv venv'

# Segundo passo #

Instanciar a maquina virtual python via comando abaixo:

'python -m venv venv'

_________________________________________________________________________________________________________________________________________________________________________________

# Third step #

At the root of the project, run the project dependencies listed in the requirements.txt file through the commands below;
After that run the migrations.

'venv/Scripts/activate'

'pip install -r requirements.txt'

'python manage.py migrate'

# Terceiro passo #

Na raiz do projeto rodar as dependencias do projeto atraves dos comandos abaixo listado no arquivo requirements.txt;
Após isso rodar as migrations.

'venv/Scripts/activate'

'pip install -r requirements.txt'

'python manage.py migrate'

_________________________________________________________________________________________________________________________________________________________________________________

# Fourth step #

Upload the Python server using the command below:

'python manage.py runserver'

# Quarto passo #

Subir o servidor Python atraves do comando abaixo:

'python manage.py runserver'

_________________________________________________________________________________________________________________________________________________________________________________

# After running all instances, in the browser at localHost 127.0.0.1 on port 8000, access the user interface to register users #

# Após rodar todas as instancias, no navegador em localHost  127.0.0.1 na porta 8000 acessar a interface do usuario para cadastro de usuarios #
