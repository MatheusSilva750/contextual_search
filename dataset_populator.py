import json
from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "test_elastic"

client = Elasticsearch(
    "http://localhost:9200",
    verify_certs=False,
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

# Define o nome do arquivo JSON
nome_do_arquivo = 'dataset.json'

try:
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
        lista_de_carros = json.load(arquivo)

    for carro in lista_de_carros:
        print(f"- {carro['modelo']} {carro['cor']}")
        client.create(index="carro", doc_type="carro", id=carro["id"], body=carro)
    print("-" * 30)

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_do_arquivo}' não foi encontrado.")
    print("Por favor, verifique se o arquivo está na mesma pasta que o script.")

except json.JSONDecodeError:
    print(f"Erro: O arquivo '{nome_do_arquivo}' não contém um JSON válido.")
    print("Por favor, verifique a formatação do arquivo.")
