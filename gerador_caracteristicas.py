from datetime import datetime
from collections import defaultdict, Counter
import statistics

def carregar_concursos_2025():
    concursos = []
    with open('resultados.txt', 'r') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split('\t')
            if len(partes) >= 17:
                concurso = partes[0]
                data = partes[1]
                data_concurso = datetime.strptime(data, '%d/%m/%Y')
                if data_concurso.year == 2025:
                    numeros = [int(n) for n in partes[2:17]]
                    concursos.append({
                        'concurso': concurso,
                        'data': data,
                        'numeros': sorted(numeros)
                    })
    return concursos

def analisar_pares_impares(concursos):
    distribuicao = []
    for concurso in concursos:
        pares = len([n for n in concurso['numeros'] if n % 2 == 0])
        impares = 15 - pares
        distribuicao.append((pares, impares))
    
    counter = Counter(distribuicao)
    print("\nDistribuição de números pares e ímpares:")
    print("-" * 60)
    for (pares, impares), quantidade in sorted(counter.items()):
        porcentagem = (quantidade / len(concursos)) * 100
        print(f"{pares} pares e {impares} ímpares: {quantidade} concursos ({porcentagem:.1f}%)")

def analisar_repeticoes_subsequentes(concursos):
    total_repeticoes = 0
    max_repeticoes = 0
    numeros_mais_repetidos = defaultdict(int)
    
    for i in range(1, len(concursos)):
        concurso_anterior = set(concursos[i-1]['numeros'])
        concurso_atual = set(concursos[i]['numeros'])
        repeticoes = concurso_anterior.intersection(concurso_atual)
        
        total_repeticoes += len(repeticoes)
        max_repeticoes = max(max_repeticoes, len(repeticoes))
        
        for num in repeticoes:
            numeros_mais_repetidos[num] += 1
    
    media_repeticoes = total_repeticoes / (len(concursos) - 1)
    
    print("\nAnálise de repetições entre concursos subsequentes:")
    print("-" * 60)
    print(f"Média de números repetidos: {media_repeticoes:.1f}")
    print(f"Máximo de números repetidos: {max_repeticoes}")
    
    print("\nNúmeros que mais se repetem em concursos subsequentes:")
    print("-" * 60)
    mais_repetidos = sorted(numeros_mais_repetidos.items(), key=lambda x: (-x[1], x[0]))[:5]
    for numero, repeticoes in mais_repetidos:
        porcentagem = (repeticoes / (len(concursos) - 1)) * 100
        print(f"Número {numero:2d}: {repeticoes} repetições ({porcentagem:.1f}% dos concursos)")

def analisar_sequencias(concursos):
    sequencias_por_concurso = []
    for concurso in concursos:
        numeros = concurso['numeros']
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
        
        sequencias_por_concurso.append(sequencias)
    
    counter = Counter(sequencias_por_concurso)
    print("\nAnálise de sequências de números consecutivos:")
    print("-" * 60)
    for sequencias, quantidade in sorted(counter.items()):
        porcentagem = (quantidade / len(concursos)) * 100
        print(f"{sequencias} sequência(s): {quantidade} concursos ({porcentagem:.1f}%)")

def analisar_soma_e_media(concursos):
    somas = []
    for concurso in concursos:
        soma = sum(concurso['numeros'])
        somas.append(soma)
    
    media_somas = statistics.mean(somas)
    mediana_somas = statistics.median(somas)
    desvio_padrao = statistics.stdev(somas)
    
    print("\nAnálise da soma dos números sorteados:")
    print("-" * 60)
    print(f"Média das somas: {media_somas:.1f}")
    print(f"Mediana das somas: {mediana_somas:.1f}")
    print(f"Desvio padrão: {desvio_padrao:.1f}")
    print(f"Menor soma: {min(somas)}")
    print(f"Maior soma: {max(somas)}")
    
    # Análise da distribuição das somas
    faixas = [(160, 170), (171, 180), (181, 190), (191, 200), (201, 210), (211, 220), (221, 230)]
    print("\nDistribuição das somas:")
    for inicio, fim in faixas:
        qtd = len([s for s in somas if inicio <= s <= fim])
        porcentagem = (qtd / len(concursos)) * 100
        print(f"Entre {inicio} e {fim}: {qtd} concursos ({porcentagem:.1f}%)")

def analisar_quadrantes(concursos):
    # Dividir os números em quadrantes (1-6, 7-12, 13-18, 19-25)
    quadrantes_contagem = []
    for concurso in concursos:
        q1 = len([n for n in concurso['numeros'] if 1 <= n <= 6])
        q2 = len([n for n in concurso['numeros'] if 7 <= n <= 12])
        q3 = len([n for n in concurso['numeros'] if 13 <= n <= 18])
        q4 = len([n for n in concurso['numeros'] if 19 <= n <= 25])
        quadrantes_contagem.append((q1, q2, q3, q4))
    
    counter = Counter(quadrantes_contagem)
    print("\nDistribuição por quadrantes (1-6, 7-12, 13-18, 19-25):")
    print("-" * 60)
    print("Distribuições mais comuns:")
    for (q1, q2, q3, q4), quantidade in sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:5]:
        porcentagem = (quantidade / len(concursos)) * 100
        print(f"Q1:{q1} Q2:{q2} Q3:{q3} Q4:{q4}: {quantidade} concursos ({porcentagem:.1f}%)")
    
    # Média por quadrante
    media_q1 = statistics.mean([q[0] for q in quadrantes_contagem])
    media_q2 = statistics.mean([q[1] for q in quadrantes_contagem])
    media_q3 = statistics.mean([q[2] for q in quadrantes_contagem])
    media_q4 = statistics.mean([q[3] for q in quadrantes_contagem])
    
    print("\nMédia de números por quadrante:")
    print(f"Q1 (1-6):    {media_q1:.1f}")
    print(f"Q2 (7-12):   {media_q2:.1f}")
    print(f"Q3 (13-18):  {media_q3:.1f}")
    print(f"Q4 (19-25):  {media_q4:.1f}")

def main():
    concursos = carregar_concursos_2025()
    total_concursos = len(concursos)
    
    if total_concursos == 0:
        print("\nNenhum concurso encontrado para o ano de 2025!")
        return
    
    primeiro_concurso = min(concursos, key=lambda x: int(x['concurso']))
    ultimo_concurso = max(concursos, key=lambda x: int(x['concurso']))
    
    print(f"\nAnálise de {total_concursos} concursos de 2025")
    print("=" * 60)
    print(f"Do concurso {primeiro_concurso['concurso']} ({primeiro_concurso['data']})")
    print(f"Até o concurso {ultimo_concurso['concurso']} ({ultimo_concurso['data']})")
    
    # Análise de números pares e ímpares
    analisar_pares_impares(concursos)
    
    # Análise de repetições em concursos subsequentes
    analisar_repeticoes_subsequentes(concursos)
    
    # Análise de sequências de números consecutivos
    analisar_sequencias(concursos)
    
    # Análise de soma e média dos números
    analisar_soma_e_media(concursos)
    
    # Análise de distribuição por quadrantes
    analisar_quadrantes(concursos)

if __name__ == "__main__":
    main()
