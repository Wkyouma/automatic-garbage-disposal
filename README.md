***Sistema de Gerenciamento e Monitoramento de Lixeiras Inteligentes***
Este projeto é uma aplicação web que utiliza tecnologias de IoT para gerenciar lixeiras inteligentes, permitindo o monitoramento em tempo real de dados como nível de preenchimento e temperatura. O sistema visa aumentar a eficiência da coleta de resíduos e promover a sustentabilidade.

**Funcionalidades**
Monitoramento em tempo real das lixeiras.
Gerenciamento de usuários com controle de acesso.
Integração com dispositivos IoT utilizando MQTT para comunicação.
Visualização do histórico de dados das lixeiras.
Detecção de lixeiras cheias e sugestão de rotas de coleta otimizadas.
Detecção de incêndios nas lixeiras.
Interface web responsiva para operadores.

**Tecnologias Utilizadas**
Flask: Framework web para Python.
SQLAlchemy: ORM utilizado para manipulação do banco de dados.
Flask-SQLAlchemy: Extensão para Flask que adiciona suporte ao SQLAlchemy.
Flask-Login: Gerenciamento de login e controle de acesso de usuários.
Flask-MQTT: Integração com o protocolo MQTT para comunicação com os sensores IoT.
HTMX: Framework front-end para manipulação de requisições HTTP dinâmicas.
SCSS: Utilizado para estilização modular e responsiva.
