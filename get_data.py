import requests

def get_data(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(endpoint)
    info_cep = response.json()
    
    return info_cep

