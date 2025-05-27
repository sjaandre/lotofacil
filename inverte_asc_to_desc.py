def processar_arquivo():
    # Lista para armazenar todas as linhas processadas
    linhas_processadas = []
    
    # Ler o arquivo original
    with open('resultados.txt', 'r') as arquivo:
        for linha in arquivo:
            # Dividir a linha em partes
            partes = linha.strip().split('\t')
            if len(partes) >= 17:  # Garantir que a linha tem todos os campos necessários
                # Armazenar a linha com o número do concurso para ordenação
                linhas_processadas.append((int(partes[0]), linha.strip()))
    
    # Ordenar as linhas pelo número do concurso em ordem decrescente
    linhas_processadas.sort(reverse=True)
    
    # Escrever o novo arquivo mantendo os números na ordem original
    with open('resultados_desc.txt', 'w') as arquivo:
        for _, linha in linhas_processadas:
            arquivo.write(linha + '\n')

if __name__ == "__main__":
    processar_arquivo()
    print("Arquivo resultados_desc.txt criado com sucesso!")
