import sys
from utils import format_json_array, KEYS
from elasticsearch import Elasticsearch
ELASTIC_PASSWORD = "test_elastic"

client = Elasticsearch(
    "http://localhost:9200",
    verify_certs=False,
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

# nome do script
script_name = sys.argv[0]
# Argumentos do usuario
user_arguments = sys.argv[1:]

print(f"Script Name: {script_name}")
print(f"User Arguments: {user_arguments}")

def get_cars_agent(terms: str) -> str:
    message = (" ").join([term for term in terms if term not in KEYS])
    def query(term):
        return {
            "query": {
                "simple_query_string": {
                    "query": message,
                    "fields": ["*"]
                }
            }
        }

    query_by_term = query(terms)
    response = client.search(body=query_by_term)
    cars = response["hits"]["hits"]
    return format_json_array(cars)

get_cars_agent(user_arguments)




