# Análise do Spotify com Python

Programa de terminal em Python que explora o dataset *Spotify Tracks* usando listas, dicionários e conjuntos, e gera gráficos com Plotly.

![Python 3.14](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-gráficos-3F4F75?logo=plotly&logoColor=white)
![Licença MIT](https://img.shields.io/badge/licença-MIT-green)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

## Sobre o trabalho

| | |
|---|---|
| Disciplina | Algoritmos e Estruturas de Dados I |
| Curso | Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) |
| Instituição | SENAC |
| Professor | Edécio Fernando Iepsen |
| Semestre | 3º semestre, 2026 |
| Atividade | Trabalho #2 (individual), apresentação em 19/10/2026 |

## Objetivo e requisitos

Praticar a manipulação de estruturas de dados (listas, dicionários e conjuntos) sobre um conjunto de dados real do Kaggle. Em resumo, o trabalho pede:

- carregar o dataset e organizá-lo em estruturas de dados da linguagem;
- oferecer um menu de terminal com diferentes consultas sobre os dados;
- usar conjuntos para comparar grupos;
- gerar gráficos a partir dos dados;
- apresentar o programa em sala.

## O dataset

[Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset), de maharshipandya, no Kaggle.

- 114.000 faixas
- 114 gêneros, com 1.000 faixas cada
- 21 colunas (incluindo uma coluna de índice sem nome)

Colunas usadas no programa:

| Coluna | Descrição |
|---|---|
| `track_id` | Identificador da faixa (usado para eliminar duplicadas) |
| `artists` | Artista(s) da faixa |
| `track_name` | Nome da música |
| `track_genre` | Gênero |
| `popularity` | Popularidade (0 a 100) |
| `explicit` | Se a faixa tem conteúdo explícito |
| `energy` | Energia |
| `danceability` | Dançabilidade |
| `valence` | Positividade musical |
| `tempo` | Andamento (BPM) |

> O arquivo CSV **não** está neste repositório (é grande e pertence a terceiros). Veja "Como rodar". Para a licença do dataset, consulte a página dele no Kaggle.

## Funcionalidades

| # | Recurso | Estrutura de dados principal |
|---|---|---|
| 1 | **Agrupar:** popularidade média por gênero (top 15) | dicionário de listas |
| 2 | **Top N:** músicas mais populares, com filtro de gênero opcional (elimina duplicadas por `track_id`) | lista ordenada + set de ids já vistos |
| 3 | **Comparar:** 2 ou mais gêneros (média de popularidade, energy, danceability, valence, BPM e contagem de explícitas) | dicionário de dicionários |
| 4 | **Conjuntos:** artistas em comum (interseção), exclusivos (diferença) e total (união) entre dois gêneros | `set` |
| 5 | **Gráfico de barras (Plotly):** top 10 gêneros por popularidade média | lista de tuplas + Plotly |
| 6 | **Gráfico de dispersão (Plotly):** energy × danceability de dois gêneros | listas paralelas + Plotly |

## Conceitos aplicados

- **Listas:** armazenar as músicas e os resultados ordenados.
- **Dicionários:** cada linha do CSV vira um dicionário; agrupamentos por gênero.
- **Conjuntos (`set`):** interseção, diferença e união de artistas; eliminação de duplicadas.
- **`sorted` com `lambda`:** ordenar por popularidade e por média.
- **`csv.DictReader`:** leitura do CSV como dicionários.
- **Plotly:** gráficos de barras e de dispersão.

## Estrutura do projeto

```
analise-spotify-python/
├── .vscode/
│   └── settings.json     # aponta o interpretador para o .venv
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── spotify.py            # programa principal
└── spotify-tracks.csv    # NÃO versionado: baixar do Kaggle
```

## Como rodar

```bash
# 1. clonar o repositório
git clone https://github.com/joaowatanabe/analise-spotify-python.git
cd analise-spotify-python

# 2. baixar o CSV no Kaggle e salvar como spotify-tracks.csv na raiz do projeto
#    https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset

# 3. criar e ativar o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 4. instalar as dependências
pip install -r requirements.txt

# 5. executar
python spotify.py
```

## Status

Em desenvolvimento.

- [ ] 1. Agrupar: popularidade média por gênero
- [ ] 2. Top N músicas
- [ ] 3. Comparar gêneros
- [ ] 4. Conjuntos de artistas
- [ ] 5. Gráfico de barras
- [ ] 6. Gráfico de dispersão

## Autor

João Vicente Watanabe, GitHub [@joaowatanabe](https://github.com/joaowatanabe).

## Licença

O **código** deste repositório é distribuído sob a licença [MIT](LICENSE). A licença cobre apenas o código: o dataset pertence ao autor original e segue a licença indicada na [página do Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset).
