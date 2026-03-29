# Script responsável pela coleta de dados
import requests
import pandas as pd

def get_data(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(endpoint)
    
    # status code 200 = OK
    if response.status_code == 200:
        info_cep = response.json()
        return info_cep
    else:
        return None

# cria a lista de CEPs a partir do arquivo users.csv
users_path = "01-bronze/users.csv"
df_users = pd.read_csv(users_path)
lista_cep = df_users['cep'].tolist()

lista_cep_info = []

# percorre a lista de CEPs e coleta a informação pela API viacep
for cep in lista_cep:
    cep = cep.replace('-','')
    info_cep = get_data(cep)
    if not "erro" in info_cep:
        lista_cep_info.append(info_cep)

df_info_cep = pd.DataFrame(lista_cep_info)
df_info_cep.to_csv("01-bronze/info_cep.csv", index=False)