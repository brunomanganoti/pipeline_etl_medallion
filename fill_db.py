import os
import pandas as pd
from db_config import DataBase
from dotenv import load_dotenv

input_dir = "02-silver"

# recupera os valores do arquivo .env
load_dotenv()
host_db = os.getenv("POSTGRES_HOST", "localhost")
port_db = os.getenv("POSTGRES_PORT", "5432")
db = os.getenv("POSTGRES_DB")
user_db = os.getenv("POSTGRES_USER")
password_db = os.getenv("POSTGRES_PASSWORD")

db = DataBase(host=host_db,
              port=port_db,
              database=db,
              user=user_db,
              password=password_db)

for file in os.listdir(input_dir):
    nome_tabela = file.replace(".parquet","")
    df = pd.read_parquet(f"{input_dir}/{file}")
    db.cria_tabela(nome_tabela, df.columns.tolist())
    db.insere_dados(nome_tabela, df)

db.close()
print("Processo finalizado.")