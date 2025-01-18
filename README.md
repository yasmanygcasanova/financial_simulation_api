# Financial Simulation API

## Descrição

A Financial Simulation API é uma aplicação desenvolvida com FastAPI que permite simular resultados financeiros com base em vendas mensais, sazonalidade, taxa de crescimento e outros parâmetros financeiros. A API fornece endpoints para simular vendas, analisar resultados financeiros e gerar gráficos baseados nas simulações.

## Funcionalidades

- Simulação de vendas ajustadas com base em sazonalidade e taxa de crescimento.
- Cálculo de métricas financeiras importantes, incluindo:
  - Ponto de equilíbrio
  - Retorno sobre investimento (ROI)
  - Margem de contribuição
- Análise de crescimento mensal.
- Geração de gráficos para visualização dos resultados.
- **Validações Rigorosas:** Validações para entradas do usuário, garantindo que os dados sejam consistentes e dentro dos limites esperados.
- **Testes Automatizados:** Testes unitários para garantir a funcionalidade correta do código.

## Estrutura do Projeto

    financial_simulation_api/
    │
    ├── app/
    │ ├── init.py
    │ ├── main.py # Arquivo principal da aplicação FastAPI
    │ ├── config.py # Carregamento e validação da configuração
    │ ├── models.py # Definição dos modelos Pydantic
    │ ├── simulation.py # Funções para simulação financeira
    │ ├── analysis.py # Funções para análise financeira
    │ ├── plotting.py # Funções para geração de gráficos
    │ └── validation/
    │ ├── init.py
    │ ├── input_validation.py # Validações das entradas do usuário
    │ ├── config_validation.py # Validações da configuração
    │ └── exceptions.py # Exceções personalizadas
    │
    ├── tests/ # Diretório para testes automatizados
    │ ├── init.py # (Opcional) Indica que este diretório é um pacote Python
    │ └── test_input_validation.py # Testes das validações de entrada
    │
    ├── requirements.txt # Dependências do projeto
    └── config.json # Arquivo de configuração em formato JSON

## Instalação

1. Clone o repositório:

        git clone https://github.com/yasmanygcasanova/financial_simulation_api.git
        cd financial-simulation-api

2. Crie um ambiente virtual:

        python -m venv venv
        source venv/bin/activate # Para Linux/Mac

3. Instale as dependências:

        pip install -r requirements.txt

4. Crie um arquivo `config.json` na raiz do projeto com a seguinte estrutura:

        {
           "BASE_MONTHLY_SALES": 10000,
           "SUPPLY_COST": 0.5,
           "PACKAGING_COST": 0.2,
           "DELIVERY_FEES": 0.1,
           "ROYALTY_PERCENTAGE": 0.05,
           "NATIONAL_MARKETING_PERCENTAGE": 0.1,
           "TAX_PERCENTAGE": 0.15,
           "FIXED_COSTS": 2000,
           "LOCAL_MARKETING_COST": 500
}

## Uso

### Para iniciar a aplicação, execute o seguinte comando:

    uvicorn app.main:app --reload --host 127.0.0.1 --port 8000



A API estará disponível em `http://localhost:8000`. 
Você pode acessar a documentação interativa da API em `http://localhost:8000/docs`.

### Endpoints

1. **POST /simulate**
   - Simula as vendas ajustadas com base na sazonalidade e taxa de crescimento.
   - **Payload:**
     ```
     {
         "seasonality": [0.1, -0.05, 0.02, 0.15, 0.2, 0.1, -0.1, -0.15, 0.05, 0.1, 0.15, 0.3],
         "growth_rate": 0.05,
         "initial_investment": 100000
     }
     ```

2. **POST /analyze**
   - Realiza a análise financeira com base nos resultados da simulação.
   - **Payload:**
     ```
     {
         "seasonality": [0.1, -0.05, 0.02, 0.15, 0.2, 0.1, -0.1, -0.15, 0.05, 0.1, 0.15, 0.3],
         "growth_rate": 0.05,
         "initial_investment": 100000
     }
     ```

3. **POST /growth-rate**
   - Calcula a taxa de crescimento mensal com base nos resultados da simulação.
   - **Payload:**
     ```
     {
         "seasonality": [0.1, -0.05, 0.02, 0.15, 0.2, 0.1, -0.1, -0.15, 0.05, 0.1, 0.15, 0.3],
         "growth_rate": 0.05,
         "initial_investment": 100000
     }
     ```

4. **POST /plot**
   - Gera um gráfico baseado nos resultados da simulação.
   - **Payload:**
     ```
     {
         "seasonality": [0.1, -0.05, 0.02, 0.15, 0.2, 0.1, -0.1, -0.15, 0.05, 0.1, 0.15, 0.3],
         "growth_rate": 0.05,
         "initial_investment": 100000
     }
     ```

## Configuração do Ambiente de Desenvolvimento

Para garantir a qualidade do código e seguir as melhores práticas de codificação, recomendamos a instalação e configuração das seguintes ferramentas:

### 1. Instalação das Bibliotecas

Instale as bibliotecas necessárias usando o pip. Execute o seguinte comando no terminal:

    pip install flake8 isort black flake8-isort

### 2. Configuração do `isort`

O `isort` é usado para organizar as importações no seu código Python. Para configurá-lo, crie um arquivo chamado `.isort.cfg` na raiz do seu projeto com o seguinte conteúdo:

    [settings]
    profile = black
    line_length = 88
    multi_line_output = 3
    include_trailing_comma = True

### 3. Configuração do `flake8`

O `flake8` é uma ferramenta de linting que verifica seu código em busca de erros de estilo e problemas potenciais. Para configurá-lo, crie um arquivo chamado `.flake8` na raiz do seu projeto com o seguinte conteúdo:

    [flake8]
    max-line-length = 88
    extend-ignore = E203, E266, E501, W503


### 4. Configuração do `black`

O `black` é um formatador de código que aplica automaticamente um estilo consistente ao seu código Python. Você pode usar a configuração padrão ou criar um arquivo `pyproject.toml` na raiz do seu projeto com o seguinte conteúdo:

    [tool.black]
    line-length = 88


### 5. Integrando com Pre-commit Hooks

Para garantir que seu código seja formatado e verificado automaticamente antes de cada commit, você pode usar pre-commit hooks. Primeiro, instale a biblioteca `pre-commit`:

    pip install pre-commit

Em seguida, crie um arquivo chamado `.pre-commit-config.yaml` na raiz do seu projeto com o seguinte conteúdo:

    repos:
    repo: https://github.com/pre-commit/mirrors-black
    rev: v21.12b0 # Use a versão mais recente disponível
    hooks:
    id: black
    repo: https://github.com/pre-commit/mirrors-isort
    rev: v5.10.3 # Use a versão mais recente disponível
    hooks:
    id: isort
    repo: https://github.com/pre-commit/mirrors-flake8
    rev: v4.1.1 # Use a versão mais recente disponível
    hooks:
    id: flake8


### 6. Instalando os Pre-commit Hooks

Depois de criar o arquivo de configuração dos pre-commit hooks, execute o seguinte comando para instalá-los:

    pre-commit install

Agora, sempre que você fizer um commit, os hooks serão executados automaticamente para formatar o código e verificar problemas de estilo.

### 7. Executando as Ferramentas Manualmente

Você também pode executar manualmente cada ferramenta para verificar ou formatar seu código:

- Para verificar o código com `flake8`:

      flake8 .

- Para organizar as importações com `isort`:

      isort .

- Para formatar o código com `black`:

      black .

## Testes Automatizados

Para executar os testes automatizados:

1. Navegue até o diretório raiz do projeto (onde está a pasta `tests`).
2. Execute o seguinte comando:

        PYTHONPATH=. pytest tests/
        pytest tests/
        pytest tests/test_input_validation.py


Isso executará todos os testes encontrados na pasta `tests`.

## Implantação no Google Cloud Run

Para implantar sua aplicação no Google Cloud Run, siga as etapas abaixo:

### 1. Pré-requisitos

- **Conta do Google Cloud:** Certifique-se de ter uma conta do Google Cloud e um projeto criado.
- **Google Cloud SDK:** Instale o Google Cloud SDK em sua máquina.
- **Autenticação:** Autentique-se usando o `gcloud` CLI.


### 2. Implantar no Google Cloud Run

Para implantar seu serviço no Cloud Run, siga estas etapas:

1. **Navegue até o diretório do seu projeto:**
        
       cd /path/to/financial_simulation/

2. **Execute o comando `gcloud run deploy`:**

Se você não estiver usando um `Dockerfile`, execute:

    gcloud run deploy SERVICE_NAME --source . --region REGION --allow-unauthenticate

Substitua `SERVICE_NAME` pelo nome desejado para seu serviço e `REGION` pela região onde deseja implantar (por exemplo, `us-central1`).

Se você estiver usando um `Dockerfile`, execute:

    gcloud builds submit --tag gcr.io/PROJECT_ID/SERVICE_NAME .
    gcloud run deploy SERVICE_NAME --image gcr.io/PROJECT_ID/SERVICE_NAME --region REGION --allow-unauthenticated

Substitua `PROJECT_ID` pelo ID do seu projeto no Google Cloud.

3. **Aguarde a conclusão da implantação:**

Após executar o comando, aguarde até que a construção e a implantação sejam concluídas. Você verá uma mensagem indicando que o serviço foi implantado com sucesso, incluindo a URL do serviço.

### 5. Acessar o Serviço

Após a implantação, você pode acessar sua aplicação através da URL fornecida na saída do comando `gcloud run deploy`. Essa URL será algo como:

    https://SERVICE_NAME-REGION.run.app

### 6. Configurações Adicionais (Opcional)

Você pode configurar variáveis de ambiente, autenticação e outras opções através do console do Google Cloud ou usando comandos adicionais no `gcloud`.


## Implementação de CI/CD

Para garantir a qualidade do código e facilitar a entrega contínua, este projeto utiliza um pipeline de CI/CD configurado com GitHub Actions. Abaixo estão as etapas para configurar e utilizar o pipeline.

### 1. Criar o Arquivo de Workflow do GitHub Actions

Crie o arquivo `ci.yml` dentro do diretório `.github/workflows/` com o seguinte conteúdo:

    name: CI/CD Pipeline
    on:
    push:
    branches:
    - main
      - develop
      pull_request:
      branches:
      - main
      - develop
      jobs:
      build:
      runs-on: ubuntu-latest


    steps:
      - name: Checkout code
        uses: actions/checkout@v2
    
        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: '3.12'
    
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
    
        - name: Run tests
          run: |
            pytest tests/
    
        - name: Build Docker image (optional)
          run: |
            docker build . -t your-image-name
    
        - name: Deploy to Cloud Run (optional)
          env:
            GOOGLE_APPLICATION_CREDENTIALS: ${{ secrets.GOOGLE_APPLICATION_CREDENTIALS }}
          run: |
            gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS 
            gcloud run deploy your-service --image your-image-name --region your-region --allow-unauthenticated


### 2. Configurar Credenciais do Google Cloud

Para permitir que o GitHub Actions implante sua aplicação no Google Cloud Run, você precisará configurar credenciais:

1. **Crie uma conta de serviço no Google Cloud** com permissões adequadas para implantar no Cloud Run.
2. **Baixe a chave JSON** dessa conta de serviço.
3. **Adicione a chave JSON como um segredo no GitHub**:
   - Vá até o repositório no GitHub.
   - Acesse **Settings** > **Secrets and variables** > **Actions** > **New repository secret**.
   - Nomeie o segredo como `GOOGLE_APPLICATION_CREDENTIALS` e cole o conteúdo da chave JSON.

### 3. Testar o Pipeline

Após configurar tudo, faça um commit e um push das suas alterações para o branch `main` ou `develop`. O GitHub Actions automaticamente iniciará o pipeline definido em `ci.yml`.

### 4. Monitorar Resultados

Você pode monitorar os resultados da execução do pipeline na aba "Actions" do seu repositório no GitHub. Isso permitirá que você veja se os testes passaram e se a implantação foi bem-sucedida.


