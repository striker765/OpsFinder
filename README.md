
OpsFinder é uma plataforma completa e eficiente que permite a equipes de TI encontrar facilmente procedimentos, jobs, hosts, servidores, e muito mais. Ele foi projetado para fornecer uma interface intuitiva para busca, gerenciamento e visualização de diversas operações críticas. Nossa aplicação foi implementada usando Django, hospedada com Docker e configurada para suportar servidores de alta performance, como Nginx e Gunicorn.

Funcionalidades
Busca Inteligente: Realize buscas rápidas por jobs, servidores, procedimentos e documentos críticos.
Organização Centralizada: Toda a infraestrutura e tarefas da equipe reunidas em um único lugar.
Interface Amigável: Fácil de navegar e encontrar o que você precisa.
Suporte a Múltiplos Usuários: Acesso a diferentes níveis de permissão para gerenciar as operações de forma segura.
CRUD no Django Admin: Gerenciamento completo de usuários e procedimentos diretamente pela interface de administração do Django, permitindo a criação, alteração e exclusão de dados.
Escalabilidade: Plataforma pronta para crescer conforme a necessidade da equipe.
Hospedagem com Docker: Deploy facilitado com Docker, tornando o ambiente de desenvolvimento e produção consistente.
Integração com Nginx e Gunicorn: Servidores otimizados para alta performance e disponibilidade.

Tecnologias Utilizadas
Backend: Django 5.1
Frontend: HTML, CSS, JavaScript
Banco de Dados: SQLite (ambiente de desenvolvimento), PostgreSQL (produção)
Servidores: Gunicorn e Nginx
Deploy: Docker
Sistema Operacional: Parrot OS

Outras Ferramentas:
Python 3.11
Git para controle de versão
Docker para containerização
Requisitos para Instalação
Docker: Certifique-se de que Docker está instalado e configurado no seu sistema.
Python 3.11+
PostgreSQL (ou banco de dados de sua preferência para produção)
Git para clonar o repositório.
Instalação e Configuração

Clone o Repositório:
bash

git clone https://github.com/striker765/opsfinder.git
cd opsfinder
Configuração do Ambiente Virtual (opcional):

bash
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

bash
pip install -r requirements.txt
Crie o banco de dados e aplique as migrações:

bash
python manage.py migrate
Configure o arquivo .env com as informações sensíveis, como chaves secretas e credenciais de banco de dados.

Execute o servidor de desenvolvimento:

bash
python manage.py runserver
Deploy em Produção com Docker:

Certifique-se de que Docker está instalado e configure o ambiente de produção utilizando o Dockerfile e o docker-compose.yml fornecidos no projeto.
bash
docker-compose up -d
O serviço estará disponível no IP público configurado no Docker.
Configuração do Nginx e Gunicorn:

No servidor de produção, o Gunicorn será utilizado como servidor WSGI, e o Nginx será configurado como proxy reverso para lidar com as requisições HTTP. Consulte os arquivos de configuração no diretório nginx/.
CRUD com Django Admin
Utilizamos o painel de administração do Django para fornecer uma interface fácil de gerenciamento para os usuários e os procedimentos. Através da interface do Django Admin, é possível realizar operações de CRUD (Criar, Ler, Atualizar e Deletar):

Usuários: Adição e remoção de usuários, além de controle sobre permissões e grupos.
Procedimentos: Gerenciamento completo de procedimentos e jobs, incluindo a criação, alteração e exclusão de registros.
Para acessar o painel de administração:

Crie um superusuário:

bash
python manage.py createsuperuser
Acesse o painel via http://localhost:8000/admin (ou substitua o localhost pelo domínio configurado).

Como Contribuir
Sinta-se à vontade para abrir issues e enviar pull requests. Toda contribuição é bem-vinda para melhorar a eficiência e funcionalidade da plataforma.

Faça um fork do projeto.
Crie uma nova branch para sua feature ou correção de bug (git checkout -b feature/nova-feature).
Commit suas mudanças (git commit -m 'Adiciona nova feature').
Faça o push da sua branch (git push origin feature/nova-feature).
Abra um Pull Request no GitHub.
Roadmap
Adicionar suporte a busca avançada com filtros.
Implementação de autenticação OAuth.
Melhoria do sistema de notificações em tempo real.
Integração com ferramentas de monitoramento, como Zabbix e Grafana.


![image](https://github.com/user-attachments/assets/869988c0-d693-42fc-b2e0-7b0e98d2a3af)

![image](https://github.com/user-attachments/assets/ad1caaa0-9156-417d-9b17-b86bb0e09fb0)

![image](https://github.com/user-attachments/assets/5f519ca6-858d-4038-9568-cb0d01dbe343)

![image](https://github.com/user-attachments/assets/70f55bb0-d180-4957-8948-f793b10d7147)
