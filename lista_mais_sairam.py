from collections import Counter

def analisar_numeros():
    # Dicionário para contar a frequência de cada número
    numeros = []
    
    # Ler o arquivo de resultados
    with open('resultados.txt', 'r') as arquivo:
        for linha in arquivo:
            # Dividir a linha em partes
            partes = linha.strip().split('\t')
            if len(partes) >= 17:  # Garantir que a linha tem todos os campos necessários
                # Pegar apenas os números (começam no índice 2)
                numeros_sorteio = [int(n) for n in partes[2:]]
                numeros.extend(numeros_sorteio)
    
    # Contar a frequência de cada número
    contagem = Counter(numeros)
    
    # Ordenar por frequência (do mais frequente para o menos frequente)
    numeros_ordenados = sorted(contagem.items(), key=lambda x: (-x[1], x[0]))
    
    # Imprimir os resultados
    print("\nNúmeros que mais saíram na Lotofácil:")
    print("\nNúmero | Quantidade de vezes sorteado")
    print("-" * 35)
    
    for numero, quantidade in numeros_ordenados:
        print(f"{numero:6d} | {quantidade:d}")

if __name__ == "__main__":
    analisar_numeros()
