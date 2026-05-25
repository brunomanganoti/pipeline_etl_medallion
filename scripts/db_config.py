# Classe DataBase para realizar operações no banco de dados
import pandas as pd
import psycopg2

class DataBase:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conexao = psycopg2.connect(host=self.host,
                                     port=self.port,
                                     database=self.database,
                                     user=self.user,
                                     password=self.password)
        
    def cria_tabela(self, nome_tabela, columns):
        cursor = self.conexao.cursor()
        colunas_tipadas = [f"{coluna} TEXT" for coluna in columns]
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({', '.join(colunas_tipadas)})")
        self.conexao.commit()
        cursor.close()

    def insere_dados(self, nome_tabela, df):
        cursor = self.conexao.cursor()
        placeholders = ', '.join(["%s"] * len(df.columns))
        insert = f"INSERT INTO {nome_tabela} VALUES ({placeholders})"
        for row in df.itertuples(index=False, name=None):
            cursor.execute(insert, row)
        self.conexao.commit()
        cursor.close()

    def executa_query(self, query):
        cursor = self.conexao.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def select_all_tabela(self, nome_tabela, limite=10):
        query = f"SELECT * FROM {nome_tabela} LIMIT {limite}"
        return self.executa_query(query)

    def close(self):
        self.conexao.close()