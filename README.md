# Django Boilerplate com Poetry e Estrutura `/src`

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://www.python.org/) [![Django](https://img.shields.io/badge/Django-5.x-green?logo=django&logoColor=white)](https://www.djangoproject.com/) [![Poetry](https://img.shields.io/badge/Poetry-1.8+-purple?logo=poetry&logoColor=white)](https://python-poetry.org/) [![Licença](https://img.shields.io/badge/Licença-MIT-lightgrey.svg)](https://opensource.org/licenses/MIT)

Este repositório fornece um template (boilerplate) para iniciar projetos Django de forma rápida e organizada, utilizando o gerenciador de dependências Poetry e adotando a estrutura de código fonte dentro da pasta `/src`.

**Objetivo:** Acelerar o início de novos projetos Django, oferecendo uma base configurada com boas práticas, economizando tempo de setup inicial e garantindo uma estrutura consistente.

## ✨ Principais Características

*   **Estrutura `/src`:** Organiza o código fonte do projeto, separando-o de arquivos de configuração, o que melhora a organização e facilita o deploy.
*   **Poetry:** Gerenciamento de dependências moderno e determinístico, garantindo ambientes virtuais consistentes.
*   **Configuração Django Básica:** Inclui configurações essenciais no `settings.py` e estrutura de URLs inicial.
*   **App `core`:** Um aplicativo inicial (`core`) já criado e configurado, com uma view e template de exemplo (`home.html`) para rápida verificação.
*   **Templates e Estáticos:** Estrutura básica para templates globais (`base_templates`) e arquivos estáticos (`base_static`, `core/static`).
*   **Variáveis de Ambiente:** Utiliza `python-dotenv` (implícito pelo Poetry) para carregar configurações de um arquivo `.env` (exemplo `.env.example` fornecido).
*   **Configuração VS Code:** Inclui configurações básicas para debug no VS Code (`.vscode/launch.json`).
*   **.gitignore:** Configurado para Python, Django e VS Code.

## 🚀 Como Usar Este Template

Siga os passos abaixo para iniciar seu projeto a partir deste boilerplate:

1.  **Clone o Repositório:**

    ```bash
    git clone https://github.com/ezerodrigues/django-boilerplate.git
    cd django-boilerplate
    ```

2.  **Instale as Dependências com Poetry:**
    (Certifique-se de ter o [Poetry](https://python-poetry.org/docs/#installation) instalado)

    ```bash
    poetry install
    ```
    Este comando criará um ambiente virtual e instalará todas as dependências listadas no `pyproject.toml`.

3.  **Configure as Variáveis de Ambiente:**
    Copie o arquivo de exemplo e ajuste as variáveis conforme necessário.

    ```bash
    cp .env.example .env
    # Edite o arquivo .env com suas configurações (SECRET_KEY, DEBUG, etc.)
    ```

4.  **Aplique as Migrações Iniciais:**
    Crie as tabelas essenciais do Django no banco de dados.

    ```bash
    poetry run python src/manage.py migrate
    ```

5.  **Crie um Superusuário (Opcional):**
    Necessário para acessar a interface de administração do Django (`/admin/`).

    ```bash
    poetry run python src/manage.py createsuperuser
    ```
    Siga as instruções no terminal para definir nome de usuário, email e senha.

6.  **Inicie o Servidor de Desenvolvimento:**

    ```bash
    poetry run python src/manage.py runserver
    ```

    Acesse `http://127.0.0.1:8000/` no seu navegador. Você deverá ver a página inicial de exemplo.

## 📁 Estrutura de Diretórios

```
.                           # Raiz do Projeto
├── .venv/                  # Ambiente virtual (gerenciado pelo Poetry)
├── .vscode/                # Configurações do VS Code (ex: launch.json)
├── base_static/
│   └── global/             # Arquivos estáticos globais (CSS, JS, Imagens)
│       └── css/
│           └── global-style.css
├── base_templates/
│   └── global/             # Templates globais (ex: base.html)
│       └── base.html
├── src/                    # Diretório principal do código fonte
│   ├── core/               # App Django de exemplo
│   │   ├── migrations/
│   │   ├── static/
│   │   │   └── core/
│   │   │       └── css/
│   │   │           └── styles.css # CSS específico do app core
│   │   ├── templates/
│   │   │   └── core/
│   │   │       ├── pages/
│   │   │       │   └── home.html  # Template da página inicial
│   │   │       └── partials/      # Partials do app core (opcional)
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── project/            # Projeto Django (configurações)
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py     # Arquivo principal de configurações
│   │   ├── urls.py         # URLs principais do projeto
│   │   └── wsgi.py
│   └── manage.py           # Utilitário de linha de comando do Django
├── tests/                  # Testes (configuração inicial)
├── .env.example            # Exemplo de arquivo de variáveis de ambiente
├── .gitignore              # Arquivos ignorados pelo Git
├── db.sqlite3              # Banco de dados SQLite (padrão)
├── poetry.lock             # Arquivo de lock do Poetry
├── pyproject.toml          # Arquivo de configuração do Poetry e do projeto
└── README.md               # Este arquivo
```

## 🔄 Próximos Passos e Personalização

Ao usar este template para um novo projeto:

1.  **Renomeie o Projeto/Apps (Opcional):** Se desejar, renomeie o diretório do projeto (`src/project`) e o app `core`. Lembre-se de atualizar as referências em `settings.py`, `wsgi.py`, `asgi.py`, `manage.py` e nos `INSTALLED_APPS`.
2.  **Crie Novos Apps:** Use `poetry run python src/manage.py startapp nome_do_app` dentro de `src/` e adicione o novo app aos `INSTALLED_APPS`.
3.  **Atualize `.env`:** Defina as variáveis de ambiente específicas do seu projeto.
4.  **Desenvolva seus Modelos:** Crie seus modelos no `models.py` dos seus apps.
5.  **Crie Migrações:** Rode `poetry run python src/manage.py makemigrations` após criar ou alterar modelos.
6.  **Aplique Migrações:** Rode `poetry run python src/manage.py migrate` para atualizar o banco de dados.
7.  **Desenvolva suas Views, Templates e URLs.**
8.  **Atualize este README.md:** Descreva seu projeto, instruções específicas, etc.

## 💡 Possíveis Melhorias Futuras para o Boilerplate

Este template pode ser estendido com:

*   **Autenticação Completa:** Usar `django-allauth` para login/registro/recuperação de senha.
*   **Testes:** Configurar `pytest-django` e adicionar exemplos de testes.
*   **Qualidade de Código:** Integrar `Ruff`, `Black`, `isort`.
*   **Docker:** Adicionar `Dockerfile` e `docker-compose.yml`.
*   **CI/CD:** Configurar GitHub Actions ou similar.
*   **Páginas de Erro:** Templates personalizados para 404 e 500.

## 📄 Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo `LICENSE` (se existir) para mais detalhes.

