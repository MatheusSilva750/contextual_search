import json
from typing import Any
KEYS = [
    "score",
    "marca",
    "modelo",
    "ano",
    "cor",
    "motor",
    "potencia_cv",
    "cambio",
    "combustivel",
    "preco_brl",
    "quilometragem"
]

def format_car(element: dict) -> str:
    props = element["_source"]
    props["score"] = element["_score"]
    message = []
    for key in KEYS:
        value = props[key]
        message.append(f"{key}: {value}")

    return_message = '\n'.join(message)
    return return_message 

def format_json_array(data: dict) -> str: 
    if(data == [] or data == None):
        return "Sem dados de carros com os atributos passados"

    messages = [format_car(element) for element in data]
    return_message = '\n---\n'.join(messages)
    print(return_message)


