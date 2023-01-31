# Python Unittest com Pokemons
- Neste repositório, estudaremos a implementação de testes unitários, de um módulo que faz requisição a uma api, interpreta seu response, e salve em um banco de dados (mongo).
- O objetivo é demonstrar como os testes unitários de fato devem ser aplicados, e o ferramental necessário para isto.
- E demonstrar como os testes unitários nos ajudam a refatorar nosso código, principalmente focando no princípio de responsabilidade única.


# Como executar

* 1. Clone o repositório:
        - git clone

* 2. Crie e ative o ambiente virtual:
        - python3 -m venv .venv
        - source .venv/bin/activate

* 3. Instale as dependências:
        - pip install -r requirements.txt

* 4. Rode os testes:
        - python -m unittest tests/run_tests.py

# Banco de dados

Como a ideia do projeto é consultar a uma api, tratar este dado e salvá-lo em um banco de dados, será necessário uma conexão com o banco de dados Mongo. Então, é necessário definir suas credentias, e subir o container do mongo. Como este repositório se trata de explorar testes unitários, os testes devem rodar independentes do banco de dados:

* 1. Definindo as credencials:
        - Crie um arquivo .env, utilizando como exemplo o .env_sample;

* 2. Levantando o banco de dados:
        - docker-compose up --build
