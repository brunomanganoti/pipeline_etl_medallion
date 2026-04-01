<h1 align="center">🏅 Pipeline ETL - Arquitetura Medalhão</h1>

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*u_C7KnKmerrfqVp0D6MG4Q.png" alt="Arquitetura Medalhão" width="650">
</p>
<p align="center">
  <em>Fonte: <a href="https://medium.com/@s19804/understanding-the-medallion-architecture-bronze-silver-and-gold-layers-09c953905d44">Medium</a></em>
</p>

* Este projeto consiste em um pipeline de dados ETL (Extract, Transform, Load) ponta a ponta local, construído em Python e estruturado com base nos conceitos da Arquitetura Medalhão (Camadas Bronze, Silver e Gold).
* O objetivo principal é demonstrar a extração de dados brutos de arquivos locais, a normalização e conversão para formatos analíticos otimizados, e o carregamento final em um banco de dados relacional isolado em contêiner.

## Arquitetura do projeto

O fluxo de dados segue as seguintes etapas:

1. **Camada Bronze:** Armazenamento dos dados brutos e originais nos formatos `.csv` e `.json`.
2. **Camada Silver:** Leitura, limpeza e conversão dos dados brutos para o formato colunar `.parquet`, garantindo tipagem correta e otimização de leitura.
3. **Camada Gold:** Carregamento dos dados processados da camada Silver para tabelas estruturadas em um banco de dados PostgreSQL, prontos para consumo por ferramentas de BI ou análises complexas.

## Tecnologias utilizadas

* **Linguagem:** Python 3.10+
* **Manipulação de Dados:** Pandas, PyArrow
* **Banco de Dados:** PostgreSQL
* **Integração:** psycopg2, SQLAlchemy
* **Infraestrutura e Ambiente:** Docker, python-dotenv

## Estrutura do repositório

* `01-bronze/`: Diretório destinado aos arquivos de dados brutos.
* `02-silver/`: Diretório de destino dos arquivos processados em formato Parquet.
* `03-gold/`: Scripts SQL e notebooks de visualização dos dados finais.
* `get_data.py`: Script responsável por consultar a API do ViaCEP para extrair dados de localização em massa e salvar os resultados brutos na camada Bronze.
* `norm_data.py`: Script responsável por converter os dados da camada Bronze para a Silver.
* `db_config.py`: Classe de conexão e manipulação de dados no PostgreSQL.
* `fill_db.py`: Script que varre a camada Silver, lê os arquivos processados em Parquet e preenche as tabelas no PostgreSQL para formar a camada Gold.
* `docker-compose.yml`: Arquivo de orquestração do banco de dados local.
* `.env.example`: Template de variáveis de ambiente.

## Executando localmente

### 1. Pré-requisitos
Ter o Python 3 e o Docker instalados em sua máquina.

### 2. Configuração do ambiente
Clone o repositório e crie o seu arquivo de configuração de variáveis de ambiente:

1. Renomeie o arquivo `.env.example` para `.env`.
2. Preencha o arquivo `.env` com as suas credenciais locais (usuário, senha, nome do banco de dados etc.).

### 3. Subindo o Banco de Dados
Inicie o contêiner do PostgreSQL utilizando o Docker Compose:

```bash
docker-compose up
```

### 4. Instalação das dependências
Instale as bibliotecas Python necessárias:

```bash
pip install -r requisitos.txt
```

### 5. Execução do pipeline
Com o banco rodando e as dependências instaladas, execute os scripts de normalização e inserção de dados. Opcionalmente, utilize o Jupyter Notebook na camada Gold para consultar e visualizar a tabela final.