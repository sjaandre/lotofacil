from collections import Counter
from itertools import combinations

def analisar_quartetos_ultimos_100():
    # Lista para armazenar todas as linhas
    todas_linhas = []
    
    # Ler o arquivo de resultados
    with open('resultados.txt', 'r') as arquivo:
        todas_linhas = arquivo.readlines()
    
    # Pegar apenas os últimos 100 concursos
    ultimos_100 = todas_linhas[-100:]
    
    # Lista para armazenar os grupos de 4 números
    grupos_numeros = []
    
    # Processar cada linha dos últimos 100 concursos
    for linha in ultimos_100:
        # Dividir a linha em partes
        partes = linha.strip().split('\t')
        if len(partes) >= 17:  # Garantir que a linha tem todos os campos necessários
            # Pegar apenas os números (começam no índice 2)
            numeros_sorteio = [int(n) for n in partes[2:]]
            # Gerar todas as combinações possíveis de 4 números
            grupos = list(combinations(sorted(numeros_sorteio), 4))
            grupos_numeros.extend(grupos)
    
    # Contar a frequência de cada grupo
    contagem = Counter(grupos_numeros)
    
    # Ordenar por frequência (do mais frequente para o menos frequente)
    grupos_ordenados = sorted(contagem.items(), key=lambda x: (-x[1], x[0]))
    
    # Imprimir os resultados
    print("\nGrupos de 4 números que mais saíram juntos nos últimos 100 concursos da Lotofácil:")
    print("\nGrupo de números     | Quantidade de vezes sorteados juntos")
    print("-" * 60)
    
    # Mostrar os 15 grupos mais frequentes
    for (num1, num2, num3, num4), quantidade in grupos_ordenados[:15]:
        print(f"{num1:2d}, {num2:2d}, {num3:2d}, {num4:2d}        | {quantidade:d}")
    
    # Mostrar também o primeiro e último concurso analisado
    primeiro_concurso = ultimos_100[0].split('\t')[0]
    ultimo_concurso = ultimos_100[-1].split('\t')[0]
    print(f"\nAnálise do concurso {primeiro_concurso} até o {ultimo_concurso}")

if __name__ == "__main__":
    analisar_quartetos_ultimos_100()
