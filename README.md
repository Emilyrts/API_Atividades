📚 API Atividades
A API Atividades é responsável por gerenciar e exibir as atividades de professores em um sistema educacional. Esta API faz parte de um ecossistema maior e depende da API Gestão Escolar, que fornece os dados essenciais relacionados aos professores e turmas.

⚙️ Funcionalidades
Consulta de atividades atribuídas a professores.

Associação entre atividades e turmas.

Integração com a API Gestão Escolar para validação de dados e vinculação com professores.

Endpoints Principais

GET	/atividades	Lista todas as atividades

GET	/atividades/{id}	Detalha uma atividade específica

DELETE	/atividades/{id}	Remove uma atividade

🧩 Dependência
Esta API depende diretamente da API Gestão Escolar (https://github.com/MIH005/api_flask.git) para:

Recuperar informações de professores.

Validar dados relacionados a usuários do sistema.

Garantir integridade e consistência entre os módulos da aplicação.

🔗 Relação com a Gestão Escolar
A integração é feita através de requisições HTTP (REST) para endpoints da API Gestão Escolar, garantindo que as atividades estejam sempre associadas a professores existentes e turmas válidas.

🚀 Tecnologias Utilizadas
Python 

API RESTful

Banco de dados (SQLAlchemy)
