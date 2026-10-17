import csv

# PASSO 1: carregar o CSV numa lista de dicionários
# Cada linha do arquivo vira um dicionário: {'track_name': 'Comedy', 'artists': 'Gen Hoshino', ...}
musicas = []

with open("spotify-tracks.csv", mode="r", encoding="utf-8") as arq:
    dados_csv = csv.DictReader(arq)
    for linha in dados_csv:
        musicas.append(linha)

print(f"Total de músicas carregadas: {len(musicas)}")


# PASSO 2: função de título + esqueleto do menu
def titulo(texto):
    print()
    print(texto)
    print("-"*40)

def agrupar_generos():
    titulo("Popularidade Média por Gênero (Top 15)")
    print("Em construção...")

def top_musicas():
  titulo("Top Músicas Mais Populares")
  print("Em construção...")

def comparar_generos():
  titulo("Comparar Gêneros")
  print("Em construção...")

def artistas_conjuntos():
    titulo("Artistas em Comum entre Gêneros")
    print("Em construção...")

def grafico_barras():
    titulo("Gráfico: Top 10 Gêneros Mais Populares")
    print("Em construção...")

def grafico_dispersao():
    titulo("Gráfico: Energia x Dançabilidade")
    print("Em construção...")

opcoes = {
    "1": agrupar_generos,
    "2": top_musicas,
    "3": comparar_generos,
    "4": artistas_conjuntos,
    "5": grafico_barras,
    "6": grafico_dispersao,
}

while True:
    titulo("Análise de Músicas do Spotify")

    print("1. Popularidade média por gênero")
    print("2. Top músicas mais populares")
    print("3. Comparar gêneros")
    print("4. Artistas em comum entre gêneros")
    print("5. Gráfico: top 10 gêneros")
    print("6. Gráfico: energia x dançabilidade")
    print("7. Finalizar")

    opcao = input("Opção: ")

    if opcao in opcoes:
        opcoes[opcao]()
    elif opcao == "7":
        break
    else:
        print("Opção inválida!")
