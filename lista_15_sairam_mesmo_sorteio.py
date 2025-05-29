from collections import Counter
from itertools import combinations
from typing import List, Tuple

def formatar_numeros(numeros: List[int]) -> str:
    return ", ".join(f"{n:2d}" for n in numeros)

def analisar_grupos_10():
    # Lista para armazenar todos os grupos de 10 números
    grupos_numeros = []
    
    # Ler o arquivo de resultados
    with open('resultados.txt', 'r') as arquivo:
        for linha in arquivo:
            # Dividir a linha em partes
            partes = linha.strip().split('\t')
            if len(partes) >= 17:  # Garantir que a linha tem todos os campos necessários
                concurso = partes[0]
                data = partes[1]
                # Pegar apenas os números (começam no índice 2)
                numeros_sorteio = [int(n) for n in partes[2:]]
                # Gerar todas as combinações possíveis de 10 números
                grupos = list(combinations(sorted(numeros_sorteio), 10))
                # Guardar o concurso e data junto com cada grupo
                for grupo in grupos:
                    grupos_numeros.append((grupo, concurso, data))
    
    # Contar a frequência de cada grupo de 10 números
    contagem = {}
    for grupo, concurso, data in grupos_numeros:
        if grupo not in contagem:
            contagem[grupo] = {'quantidade': 0, 'concursos': []}
        contagem[grupo]['quantidade'] += 1
        contagem[grupo]['concursos'].append((concurso, data))
    
    # Ordenar por frequência (do mais frequente para o menos frequente)
    grupos_ordenados = sorted(contagem.items(), key=lambda x: (-x[1]['quantidade'], x[0]))
    
    # Imprimir os resultados
    print("\nGrupos de 10 números que mais saíram juntos em toda a história da Lotofácil:")
    print("\nNúmeros do grupo                                    | Quantidade | Últimos concursos onde apareceram (máx. 3)")
    print("-" * 100)
    
    # Mostrar os 20 grupos mais frequentes
    for grupo, info in grupos_ordenados[:20]:
        # Pegar os 3 concursos mais recentes onde o grupo apareceu
        ultimos_concursos = info['concursos'][-3:]
        detalhes_concursos = [f"{conc} ({data})" for conc, data in ultimos_concursos]
        
        print(f"{formatar_numeros(grupo)} | {info['quantidade']:10d} | {', '.join(detalhes_concursos)}")
    
    # Mostrar estatísticas gerais
    total_grupos = len(grupos_ordenados)
    print(f"\nEstatísticas gerais:")
    print(f"Total de combinações diferentes de 10 números encontradas: {total_grupos}")
    print(f"Quantidade de vezes que o grupo mais frequente apareceu: {grupos_ordenados[0][1]['quantidade']}")

if __name__ == "__main__":
    analisar_grupos_10()
