# Contextual Search

Este projeto utiliza Docker, Docker Compose, Python 3 e Elasticsearch para realizar buscas contextuais em datasets.

## Dependências

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3](https://www.python.org/)

## Instalação

1. **Clone o repositório**

   ```bash
   git clone https://github.com/MatheusSilva750/contextual_search.git
   cd contextual_search
   ```

2. **Instale os pacotes Python**

   ```bash
   pip install -r requirements.txt
   ```

3. **Suba o Elasticsearch localmente com Docker Compose**

   ```bash
   docker-compose up
   ```

## Utilização

1. **Popule o dataset**

   ```bash
   python3 dataset_populator.py
   ```

2. **Execute o agente de busca**

   ```bash
   python3 seacher_agent.py "sua busca aqui"
   ```

   Substitua `"sua busca aqui"` pelo termo que deseja pesquisar.

---
