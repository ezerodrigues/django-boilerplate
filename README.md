# Django Boilerplate com Poetry e Estrutura `/src`

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-4.2%2B-green)
![Poetry](https://img.shields.io/badge/Poetry-1.5%2B-purple)
![Licença](https://img.shields.io/badge/Licença-MIT-yellow)

Este repositório é um template profissional para iniciar projetos Django já configurados com o gerenciador de dependências Poetry, estrutura de código fonte dentro da pasta `/src`, configurações para VS Code, variáveis de ambiente e boas práticas de desenvolvimento. O objetivo deste boilerplate é proporcionar um ponto de partida sólido para seus projetos Django, economizando tempo de configuração inicial e garantindo que você comece com uma estrutura organizada e seguindo as melhores práticas da comunidade.

## 📋 Descrição do Projeto

Este boilerplate foi cuidadosamente estruturado para oferecer uma base robusta para seus projetos Django. A estrutura `/src` foi escolhida para evitar imports acidentais e facilitar o processo de deploy, mantendo uma clara separação entre o código da aplicação e arquivos de configuração do projeto. O Poetry foi integrado como gerenciador de dependências para garantir ambientes virtuais consistentes e reproduzíveis, facilitando o controle preciso das versões de pacotes utilizados no projeto.

O template inclui um app core já configurado com uma view de exemplo (Hello World) para que você possa verificar rapidamente se tudo está funcionando corretamente. Além disso, o projeto vem com configurações prontas para o VS Code, permitindo debug eficiente diretamente do editor. A estrutura de variáveis de ambiente também está implementada, seguindo as melhores práticas de segurança para manter informações sensíveis fora do controle de versão.

## 🚀 Como Usar Este Template

Para começar a utilizar este template em seus projetos, siga as instruções detalhadas abaixo. O processo é simples e rápido, permitindo que você tenha um ambiente Django funcional em poucos minutos.

### Clonando o Repositório

O primeiro passo é clonar este repositório para sua máquina local. Abra seu terminal e execute o seguinte comando:

```bash
git clone git@github.com:SEU_USUARIO/django-boilerplate.git
cd django-boilerplate
```

Substitua `SEU_USUARIO` pelo seu nome de usuário no GitHub. Este comando irá baixar todos os arquivos do template para sua máquina e navegar para o diretório do projeto.

### Instalando Dependências

Com o Poetry já instalado em seu sistema, a instalação das dependências do projeto é extremamente simples. No diretório raiz do projeto, execute:

```bash
poetry install
```

Este comando criará um ambiente virtual e instalará todas as dependências listadas no arquivo `pyproject.toml`. O Poetry gerencia automaticamente o ambiente virtual, então você não precisa se preocupar em ativá-lo manualmente.

### Configurando Variáveis de Ambiente

O template utiliza variáveis de ambiente para configurações sensíveis. Um arquivo de exemplo `.env.example` está incluído no repositório. Você deve criar seu próprio arquivo `.env` baseado neste exemplo:

```bash
cp .env.example .env
```

Abra o arquivo `.env` em seu editor de texto preferido e ajuste as variáveis conforme necessário para seu projeto.

### Executando Migrações

Antes de iniciar o servidor, é necessário aplicar as migrações iniciais do Django. Execute o seguinte comando:

```bash
poetry run python src/manage.py migrate
```

Este comando aplicará todas as migrações pendentes, criando as tabelas necessárias no banco de dados.

### Iniciando o Servidor de Desenvolvimento

Agora você está pronto para iniciar o servidor de desenvolvimento do Django:

```bash
poetry run python src/manage.py runserver
```

O servidor será iniciado e estará acessível em `http://localhost:8000/`. Para verificar se tudo está funcionando corretamente, acesse a rota de teste em `http://localhost:8000/hello/`. Você deverá ver a mensagem "Hello, World!" na tela.

## 📁 Estrutura do Projeto

A estrutura de diretórios deste template foi cuidadosamente planejada para promover organização e seguir as melhores práticas de desenvolvimento Django. Abaixo está uma visão geral da estrutura:

```
src/
  config/        # Projeto Django (settings.py, urls.py etc)
  core/          # App exemplo
    views.py     # Inclui view de teste (Hello World)
    urls.py      # Inclui rota /hello/
    templates/
      core/
        example.html
tests/           # Testes globais (opcional)
.vscode/         # Configuração de debug do VS Code
.env.example     # Exemplo de variáveis de ambiente
.gitignore
README.md
pyproject.toml
poetry.lock
```

O diretório `src/` contém todo o código fonte do projeto, com o projeto Django principal na pasta `config/` e um app de exemplo na pasta `core/`. A pasta `tests/` é destinada a testes globais que abrangem múltiplos apps. Os arquivos de configuração do Poetry (`pyproject.toml` e `poetry.lock`) estão na raiz do projeto, junto com arquivos de configuração do VS Code e do Git.

## 🔄 O Que Fazer ao Criar um Novo Projeto

Ao utilizar este template como base para um novo projeto, recomendamos seguir estes passos para personalização:

### Renomeando o Projeto

Se desejar, você pode renomear o diretório do projeto Django em `src/config/` para o nome do seu novo projeto. Lembre-se de atualizar todas as referências a este nome em arquivos como `settings.py`, `wsgi.py`, `asgi.py` e outros.

### Criando Novos Apps

Você pode criar novos apps conforme necessário para seu projeto. Para manter a estrutura organizada, recomendamos criar os apps dentro do diretório `src/`:

```bash
cd src
poetry run python manage.py startapp nome_do_app
```

Lembre-se de adicionar o novo app à lista `INSTALLED_APPS` no arquivo `settings.py`.

### Atualizando Variáveis de Ambiente

Revise e atualize o arquivo `.env` com as variáveis específicas do seu projeto, como credenciais de banco de dados, chaves secretas e configurações de serviços externos.

### Removendo o Exemplo Hello World

O template inclui uma view de exemplo (Hello World) para demonstração. Quando estiver pronto para desenvolver seu próprio projeto, você pode remover ou modificar esta view e suas rotas associadas.

### Atualizando o README

Não se esqueça de atualizar este README.md para refletir as especificidades do seu novo projeto, incluindo descrição, instruções de instalação e uso, e outras informações relevantes.

## 🧩 Recursos Inclusos

Este template Django inclui diversos recursos que facilitam o início rápido de novos projetos:

### Estrutura `/src`

A estrutura de código fonte dentro da pasta `/src` evita imports acidentais e facilita o deploy, seguindo as recomendações da PyPA (Python Packaging Authority). Esta organização proporciona uma clara separação entre código da aplicação e arquivos de configuração.

### Configuração com Poetry

O Poetry oferece um gerenciamento de dependências moderno e eficiente, com resolução de dependências determinística e ambientes virtuais isolados. O arquivo `pyproject.toml` já está configurado com as dependências básicas para um projeto Django.

### App Core com Exemplo

Um app core já está criado e configurado, incluindo uma view de exemplo e uma rota para demonstração. Isto permite verificar rapidamente se o ambiente está funcionando corretamente.

### Templates HTML

O template inclui um exemplo básico de template HTML, demonstrando a estrutura de diretórios recomendada para templates em projetos Django.

### Debug pelo VS Code

Configurações prontas para debug no VS Code estão incluídas no diretório `.vscode/`, permitindo depurar seu código Django diretamente do editor com breakpoints e inspeção de variáveis.

### Variáveis de Ambiente

Um arquivo `.env.example` está incluído para demonstrar como configurar variáveis de ambiente para seu projeto, seguindo as melhores práticas de segurança para informações sensíveis.

### Gitignore Completo

O arquivo `.gitignore` já está configurado para Python, VS Code e Django, garantindo que arquivos temporários, caches, ambientes virtuais e outros arquivos desnecessários não sejam incluídos no controle de versão.

## 📚 Referências

Para aprofundar seus conhecimentos sobre as tecnologias e práticas utilizadas neste template, recomendamos consultar as seguintes referências:

### Documentação Django

A documentação oficial do Django é um recurso valioso para aprender sobre o framework e suas funcionalidades. Visite [https://docs.djangoproject.com/](https://docs.djangoproject.com/) para acessar a documentação completa.

### Documentação Poetry

Para entender melhor como utilizar o Poetry para gerenciamento de dependências, consulte a documentação oficial em [https://python-poetry.org/docs/](https://python-poetry.org/docs/).

### Boas Práticas com src layout

A estrutura `/src` segue as recomendações da PyPA (Python Packaging Authority) para organização de projetos Python. Saiba mais em [https://packaging.python.org/en/latest/tutorials/packaging-projects/](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

---

⭐ Se este template foi útil para você, considere dar uma estrela no repositório!

**Eliézer Rodrigues**

GitHub: [ezerodrigues](https://github.com/ezerodrigues)
