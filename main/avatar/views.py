
from django.shortcuts import render
import requests
from translate import Translator

# Create your views here.
def characters(request):
    # URL da API de Avatar
    page = request.GET.get('page', 1)
    items_per_page = 8
    url = f'https://last-airbender-api.fly.dev/api/v1/characters?perPage={items_per_page}&page={page}'

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
    else:
        print(f"Erro ao fazer a requisição. Status code: {response.status_code}")

    return render(request, "index.html", {'data': data, 'page': int(page)})