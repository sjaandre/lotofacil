from collections import Counter
from itertools import combinations

def analisar_pares_ultimos_100():
    # Lista para armazenar todas as linhas
    todas_linhas = []
    
    # Ler o arquivo de resultados
    with open('resultados.txt', 'r') as arquivo:
        todas_linhas = arquivo.readlines()
    
    # Pegar apenas os últimos 100 concursos
    ultimos_100 = todas_linhas[-100:]
    
    # Lista para armazenar os pares de números
    pares_numeros = []
    
    # Processar cada linha dos últimos 100 concursos
    for linha in ultimos_100:
        # Dividir a linha em partes
        partes = linha.strip().split('\t')
        if len(partes) >= 17:  # Garantir que a linha tem todos os campos necessários
            # Pegar apenas os números (começam no índice 2)
            numeros_sorteio = [int(n) for n in partes[2:]]
            # Gerar todas as combinações possíveis de pares
            pares = list(combinations(sorted(numeros_sorteio), 2))
            pares_numeros.extend(pares)
    
    # Contar a frequência de cada par
    contagem = Counter(pares_numeros)
    
    # Ordenar por frequência (do mais frequente para o menos frequente)
    pares_ordenados = sorted(contagem.items(), key=lambda x: (-x[1], x[0]))
    
    # Imprimir os resultados
    print("\nPares de números que mais saíram juntos nos últimos 100 concursos da Lotofácil:")
    print("\nPar de números | Quantidade de vezes sorteados juntos")
    print("-" * 50)
    
    # Mostrar os 20 pares mais frequentes
    for (num1, num2), quantidade in pares_ordenados[:20]:
        print(f"{num1:2d} e {num2:2d}      | {quantidade:d}")
    
    # Mostrar também o primeiro e último concurso analisado
    primeiro_concurso = ultimos_100[0].split('\t')[0]
    ultimo_concurso = ultimos_100[-1].split('\t')[0]
    print(f"\nAnálise do concurso {primeiro_concurso} até o {ultimo_concurso}")

if __name__ == "__main__":
    analisar_pares_ultimos_100()
