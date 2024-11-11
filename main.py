import requests
import json
from translate import Translator

# URL da API de Avatar
url = "https://last-airbender-api.fly.dev/api/v1/characters"

# Fazendo a requisição GET
response = requests.get(url)

# Inicializando o tradutor
translator = Translator(to_lang='pt')

# Verificando se a requisição foi bem-sucedida (status 200)
if response.status_code == 200:
    # Pegando o JSON da resposta
    data = response.json()
    
    # Traduzindo os atributos 'name' e 'affiliation' para português
    for character in data:
        if 'name' in character:
            character['name'] = translator.translate(character['name'])
        if 'affiliation' in character and character['affiliation']:
            character['affiliation'] = translator.translate(character['affiliation'])
    
    # Imprimindo o corpo da resposta (dados dos personagens)
    print(json.dumps(data, indent=4, sort_keys=True))
else:
    print(f"Erro ao fazer a requisição. Status code: {response.status_code}")
