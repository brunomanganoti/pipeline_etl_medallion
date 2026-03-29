import os
import pandas as pd
from db_config import DataBase
from dotenv import load_dotenv

# recupera os valores do arquivo .env
load_dotenv()
host_db = os.getenv("POSTGRES_HOST", "localhost")
port_db = os.getenv("POSTGRES_PORT", "5432")
db = os.getenv("POSTGRES_DB")
user_db = os.getenv("POSTGRES_USER")
password_db = os.getenv("POSTGRES_PASSWORD")

if __name__ == "__main__":
    db = DataBase(host=host_db, port=port_db, database=db, user=user_db, password=password_db)

    df = pd.DataFrame({"id": [1,2,3], "nomes": ["Bruno","Lucas","Sebastian"]})

    db.cria_tabela("teste", df.columns.tolist())

    db.insere_dados("teste", df)

    print(db.select_all_tabela("teste", 10))

    db.close()