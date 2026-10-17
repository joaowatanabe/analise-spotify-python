import csv

# PASSO 1: carregar o CSV numa lista de dicionários
# Cada linha do arquivo vira um dicionário: {'track_name': 'Comedy', 'artists': 'Gen Hoshino', ...}
musicas = []

with open("spotify-tracks.csv", mode="r", encoding="utf-8") as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    musicas.append(linha)

print(f"Total de músicas carregadas: {len(musicas)}")
print(musicas[0])
