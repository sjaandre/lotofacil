from collections import Counter

def analisar_ultimos_30():
    # Lista para armazenar todas as linhas
    todas_linhas = []
    
    # Ler o arquivo de resultados
    with open('resultados.txt', 'r') as arquivo:
        todas_linhas = arquivo.readlines()
    
    # Pegar apenas os últimos 30 concursos
    ultimos_30 = todas_linhas[-30:]
    
    # Lista para armazenar todos os números dos últimos 30 concursos
    numeros = []
    
    # Processar cada linha dos últimos 30 concursos
    for linha in ultimos_30:
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
    print("\nNúmeros que mais saíram nos últimos 30 concursos da Lotofácil:")
    print("\nNúmero | Quantidade de vezes sorteado")
    print("-" * 35)
    
    for numero, quantidade in numeros_ordenados:
        print(f"{numero:6d} | {quantidade:d}")
    
    # Mostrar também o primeiro e último concurso analisado
    primeiro_concurso = ultimos_30[0].split('\t')[0]
    ultimo_concurso = ultimos_30[-1].split('\t')[0]
    print(f"\nAnálise do concurso {primeiro_concurso} até o {ultimo_concurso}")

if __name__ == "__main__":
    analisar_ultimos_30()
