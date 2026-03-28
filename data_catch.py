import requests

endpoint = "https://viacep.com.br/ws/87020030/json/"

response = requests.get(endpoint)

print(response.json())