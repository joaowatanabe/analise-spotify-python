import csv
import plotly.express as px

musicas = []

with open("spotify-tracks.csv", mode="r", encoding="utf-8") as arq:
    dados_csv = csv.DictReader(arq)
    for linha in dados_csv:
        musicas.append(linha)

# conjunto com os 114 gêneros, usado para validar o que o usuário digita
generos = set(musica["track_genre"] for musica in musicas)

print(f"Total de músicas carregadas: {len(musicas)}")

def titulo(texto):
    print()
    print(texto)
    print("-"*40)

def ler_genero(texto):
    # repete a pergunta até o usuário digitar um gênero que existe
    while True:
        genero = input(texto).strip().lower()
        if genero in generos:
            return genero
        print(f"Gênero '{genero}' não existe. Exemplos: pop, rock, sertanejo, funk, mpb, k-pop")

def media_coluna(lista, coluna):
    # média de uma coluna numérica (ex.: "energy") numa lista de músicas
    total = sum(float(musica[coluna]) for musica in lista)
    return total / len(lista)

def calcular_media_popularidade():
    soma_popularidade = {}
    quantidade_genero = {}
    media = {}

    for musica in musicas:
        genero = musica["track_genre"]
        popularidade = int(musica["popularity"])

        soma_popularidade[genero] = soma_popularidade.get(genero, 0) + popularidade
        quantidade_genero[genero] = quantidade_genero.get(genero, 0) + 1

    for genero, total in soma_popularidade.items():
        media[genero] = total / quantidade_genero[genero]

    return sorted(media.items(), key=lambda item: item[1], reverse=True)

def agrupar_generos():
    titulo("Popularidade Média por Gênero (Top 15)")

    ranking = calcular_media_popularidade()

    print(f"{'Nº':>3}  {'Gênero':20s} {'Média':>5}")
    print("-" * 62)
    for posicao, (genero, valor) in enumerate(ranking[:15], start=1):
        barra = "█" * int(valor / 2)
        print(f"{posicao:2d}º  {genero:20s} {valor:5.1f}  {barra}")

def top_musicas():
    titulo("Top Músicas Mais Populares")

    n = int(input("Quantas músicas? "))

    ranking = sorted(musicas, key=lambda musica: int(musica["popularity"]), reverse=True)

    ja_vistas = set()
    posicao = 0
    print(f"{'Nº':>3}  {'Música':35s} {'Artista':25s} {'Pop.':>4}")
    print("-" * 70)

    for musica in ranking:
        if musica["track_id"] in ja_vistas:
            continue
        ja_vistas.add(musica["track_id"])
        posicao += 1
        print(f"{posicao:2d}º  {musica['track_name'][:35]:35s} {musica['artists'][:25]:25s} {musica['popularity']:>4}")

        if posicao == n:
            break

def comparar_generos():
    titulo("Comparar Gêneros")

    texto = input("Gêneros separados por vírgula (ex.: sertanejo, funk, mpb): ")
    escolhidos = []
    for genero in texto.split(","):
        genero = genero.strip().lower()
        if genero in generos and genero not in escolhidos:
            escolhidos.append(genero)
        elif genero not in generos:
            print(f"Gênero '{genero}' não existe e foi ignorado.")

    if len(escolhidos) < 2:
        print("Informe pelo menos 2 gêneros válidos.")
        return

    print()
    print(f"{'Gênero':15s} {'Qtd':>5} {'Pop.':>5} {'Energia':>8} {'Dança':>6} {'Alegria':>8} {'BPM':>6} {'Explíc.':>8}")
    print("-" * 66)

    for genero in escolhidos:
        do_genero = [musica for musica in musicas if musica["track_genre"] == genero]
        explicitas = len([musica for musica in do_genero if musica["explicit"] == "True"])

        print(f"{genero:15s} {len(do_genero):5d} "
              f"{media_coluna(do_genero, 'popularity'):5.1f} "
              f"{media_coluna(do_genero, 'energy'):8.2f} "
              f"{media_coluna(do_genero, 'danceability'):6.2f} "
              f"{media_coluna(do_genero, 'valence'):8.2f} "
              f"{media_coluna(do_genero, 'tempo'):6.1f} "
              f"{explicitas:8d}")

    print()
    print("Energia, Dança e Alegria vão de 0 a 1 · Pop. vai de 0 a 100 · Explíc. = nº de músicas explícitas")

def artistas_conjuntos():
    titulo("Artistas em Comum entre Gêneros")

    genero_a = ler_genero("1º gênero: ")
    genero_b = ler_genero("2º gênero: ")

    artistas_a = set()
    artistas_b = set()

    for musica in musicas:
        if musica["artists"] == "":
            continue
        # uma música pode ter vários artistas separados por ";"
        nomes = musica["artists"].split(";")
        if musica["track_genre"] == genero_a:
            artistas_a.update(nomes)
        if musica["track_genre"] == genero_b:
            artistas_b.update(nomes)

    em_comum = artistas_a.intersection(artistas_b)
    so_a = artistas_a.difference(artistas_b)
    so_b = artistas_b.difference(artistas_a)
    todos = artistas_a.union(artistas_b)

    print()
    print(f"Artistas de {genero_a}: {len(artistas_a)}")
    print(f"Artistas de {genero_b}: {len(artistas_b)}")
    print(f"União (total sem repetir): {len(todos)}")
    print()
    print(f"Em comum (interseção): {len(em_comum)}")
    for artista in sorted(em_comum)[:20]:
        print(f"  • {artista}")
    if len(em_comum) > 20:
        print(f"  ... e mais {len(em_comum) - 20}")
    print()
    print(f"Só em {genero_a} (diferença): {len(so_a)} · ex.: {', '.join(sorted(so_a)[:5])}")
    print(f"Só em {genero_b} (diferença): {len(so_b)} · ex.: {', '.join(sorted(so_b)[:5])}")

def grafico_barras():
    titulo("Gráfico: Top 10 Gêneros Mais Populares")

    top10 = calcular_media_popularidade()[:10]
    rotulos = [genero for genero, valor in top10]
    valores = [round(valor, 1) for genero, valor in top10]

    fig = px.bar(x=rotulos, y=valores, text=valores,
                 title="Top 10 gêneros por popularidade média no Spotify",
                 labels={"x": "Gênero", "y": "Popularidade média (0-100)"})
    fig.update_traces(marker_color="#1DB954")
    fig.show()
    print("Gráfico aberto no navegador.")

def grafico_dispersao():
    titulo("Gráfico: Energia x Dançabilidade")

    genero_a = ler_genero("1º gênero: ")
    genero_b = ler_genero("2º gênero: ")

    selecionadas = [musica for musica in musicas if musica["track_genre"] in (genero_a, genero_b)]

    fig = px.scatter(x=[float(musica["energy"]) for musica in selecionadas],
                     y=[float(musica["danceability"]) for musica in selecionadas],
                     color=[musica["track_genre"] for musica in selecionadas],
                     hover_name=[musica["track_name"] for musica in selecionadas],
                     opacity=0.6,
                     title=f"Energia x Dançabilidade: {genero_a} vs {genero_b}",
                     labels={"x": "Energia (0-1)", "y": "Dançabilidade (0-1)", "color": "Gênero"})
    fig.show()
    print("Gráfico aberto no navegador.")

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
    print("114 mil faixas · 114 gêneros · catálogo global · coleta 2022-2023")
    print(" ")
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
