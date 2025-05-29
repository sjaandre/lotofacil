import random
from collections import Counter
import statistics

def contar_pares_impares(numeros):
    pares = len([n for n in numeros if n % 2 == 0])
    impares = 15 - pares
    return pares, impares

def contar_sequencias(numeros):
    numeros = sorted(numeros)
    sequencias = 0
    sequencia_atual = 1
    
    for i in range(1, len(numeros)):
        if numeros[i] == numeros[i-1] + 1:
            sequencia_atual += 1
        else:
            if sequencia_atual > 1:
                sequencias += 1
            sequencia_atual = 1
    
    if sequencia_atual > 1:
        sequencias += 1
    
    return sequencias

def contar_quadrantes(numeros):
    q1 = len([n for n in numeros if 1 <= n <= 6])
    q2 = len([n for n in numeros if 7 <= n <= 12])
    q3 = len([n for n in numeros if 13 <= n <= 18])
    q4 = len([n for n in numeros if 19 <= n <= 25])
    return q1, q2, q3, q4

def gerar_jogo():
    # Características desejadas baseadas na análise:
    # - Entre 7-8 números pares e 7-8 ímpares
    # - 1-2 sequências de números consecutivos
    # - Soma total entre 180 e 210
    # - Distribuição equilibrada entre quadrantes (3-4 números por quadrante)
    
    while True:
        # Gerar números aleatórios
        numeros = random.sample(range(1, 26), 15)
        
        # Verificar características
        pares, impares = contar_pares_impares(numeros)
        if not (6 <= pares <= 9):  # Permitir entre 6-9 pares
            continue
            
        sequencias = contar_sequencias(numeros)
        if not (1 <= sequencias <= 2):  # Permitir 1-2 sequências
            continue
            
        soma = sum(numeros)
        if not (180 <= soma <= 210):  # Soma dentro da faixa mais comum
            continue
            
        q1, q2, q3, q4 = contar_quadrantes(numeros)
        if max(q1, q2, q3, q4) > 5 or min(q1, q2, q3, q4) < 2:  # Distribuição equilibrada
            continue
            
        return sorted(numeros)

def analisar_jogo(numeros, indice):
    print(f"\nJogo {indice + 1}:")
    print("-" * 60)
    
    # Mostrar números
    numeros_str = ", ".join(f"{n:2d}" for n in numeros)
    print(f"Números: {numeros_str}")
    
    # Pares e Ímpares
    pares, impares = contar_pares_impares(numeros)
    print(f"Pares: {pares} números ({', '.join(str(n) for n in numeros if n % 2 == 0)})")
    print(f"Ímpares: {impares} números ({', '.join(str(n) for n in numeros if n % 2 != 0)})")
    
    # Sequências
    sequencias = contar_sequencias(numeros)
    print(f"Sequências consecutivas: {sequencias}")
    
    # Soma
    soma = sum(numeros)
    print(f"Soma total: {soma}")
    
    # Quadrantes
    q1, q2, q3, q4 = contar_quadrantes(numeros)
    print(f"Distribuição por quadrantes:")
    print(f"Q1 (1-6):   {q1} números ({', '.join(str(n) for n in numeros if 1 <= n <= 6)})")
    print(f"Q2 (7-12):  {q2} números ({', '.join(str(n) for n in numeros if 7 <= n <= 12)})")
    print(f"Q3 (13-18): {q3} números ({', '.join(str(n) for n in numeros if 13 <= n <= 18)})")
    print(f"Q4 (19-25): {q4} números ({', '.join(str(n) for n in numeros if 19 <= n <= 25)})")

def mostrar_resumo_geral(jogos):
    print("\nResumo Geral dos 10 Jogos")
    print("=" * 60)
    
    # Média de pares/ímpares
    pares_por_jogo = [contar_pares_impares(jogo)[0] for jogo in jogos]
    media_pares = statistics.mean(pares_por_jogo)
    print(f"\nMédia de números pares: {media_pares:.1f}")
    
    # Média de sequências
    sequencias_por_jogo = [contar_sequencias(jogo) for jogo in jogos]
    media_sequencias = statistics.mean(sequencias_por_jogo)
    print(f"Média de sequências: {media_sequencias:.1f}")
    
    # Média das somas
    somas = [sum(jogo) for jogo in jogos]
    media_somas = statistics.mean(somas)
    print(f"Média das somas: {media_somas:.1f}")
    
    # Números mais frequentes
    todos_numeros = [num for jogo in jogos for num in jogo]
    contagem = Counter(todos_numeros)
    print("\nNúmeros mais frequentes nos 10 jogos:")
    for numero, freq in sorted(contagem.items(), key=lambda x: (-x[1], x[0]))[:5]:
        print(f"Número {numero:2d}: {freq} vezes")

def main():
    print("Gerando 10 jogos da Lotofácil com base nas características mais comuns...")
    print("=" * 60)
    
    # Gerar 10 jogos
    jogos = []
    for i in range(10):
        jogo = gerar_jogo()
        jogos.append(jogo)
        analisar_jogo(jogo, i)
    
    # Mostrar resumo geral
    mostrar_resumo_geral(jogos)

if __name__ == "__main__":
    main()
