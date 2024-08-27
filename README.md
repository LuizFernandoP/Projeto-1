# Projeto-1

Este repositório contém o código-fonte do sistema desenvolvido pelo grupo. O sistema foi construído utilizando Flask no backend e uma combinação de Bootstrap, HTML, CSS e JavaScript no frontend. O banco de dados utilizado é o SQLite.
Equipe

    Frontend: Thiago, Luiz
    Backend: Eliel, Alane, Adrielle

Ferramentas Utilizadas

    Flask: Framework web utilizado para o desenvolvimento do backend.
    SQLite: Banco de dados relacional utilizado para armazenar os dados do sistema.
    Bootstrap: Framework CSS utilizado para estilização e responsividade do frontend.
    HTML/CSS: Linguagens de marcação e estilo utilizadas para estruturar e estilizar as páginas.
    JavaScript: Linguagem de programação utilizada para interatividade e manipulação do DOM no frontend.

Pré-requisitos

Para rodar o sistema, você precisará ter os seguintes softwares instalados em sua máquina:

    Python: Versão 3.8 ou superior
    Pip: Gerenciador de pacotes do Python

Instalação

Siga os passos abaixo para configurar o ambiente e rodar o sistema localmente:

    Clone o repositório:

    bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Crie um ambiente virtual:

bash

python3 -m venv venv
source venv/bin/activate  # No Windows use venv\Scripts\activate

Instale as dependências:

bash

pip install -r requirements.txt

Configure o banco de dados:

Execute o seguinte comando para criar o banco de dados SQLite:

bash

python

python

from database import db
db.create_all()
exit()

Execute a aplicação:

bash

    python app.py

    Acesse o sistema:

    Abra o navegador e acesse http://localhost:5000 para visualizar o sistema em funcionamento.

Estrutura do Projeto

    app.py: Arquivo principal que inicia a aplicação Flask.
    /templates: Contém os arquivos HTML.
    /static: Contém arquivos CSS, JavaScript e imagens.
    /routes: Define as rotas e lógicas de negócio do backend.
    /database: Configurações e modelos do banco de dados.