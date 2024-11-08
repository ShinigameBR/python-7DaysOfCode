import requests
import json

# URL da API de Avatar
url = "https://last-airbender-api.fly.dev/api/v1/characters"

# Fazendo a requisição GET
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida (status 200)
if response.status_code == 200:
    # Pegando o JSON da resposta
    data = response.json()
    
    # Imprimindo o corpo da resposta (dados dos personagens)
    print(json.dumps(data, indent=4, sort_keys=True))
else:
    print(f"Erro ao fazer a requisição. Status code: {response.status_code}")
