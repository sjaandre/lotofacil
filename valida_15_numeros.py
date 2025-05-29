import itertools
from datetime import datetime

def validar_entrada(numeros):
    # Verifica se são entre 15 e 20 números
    if len(numeros) < 15 or len(numeros) > 20:
        return False, "Erro: Digite entre 15 e 20 números!"
    
    # Verifica se todos são números válidos (1 a 25)
    for num in numeros:
        if num < 1 or num > 25:
            return False, f"Erro: O número {num} não está entre 1 e 25!"
    
    # Verifica se não há números repetidos
    if len(set(numeros)) != len(numeros):
        return False, "Erro: Não pode haver números repetidos!"
    
    return True, "OK"

def obter_valor_premio(linha_rateio, num_acertos):
    # Índices dos valores de prêmio no arquivo rateio.txt
    indices = {
        15: 0,  # Primeira coluna (índice 0)
        14: 2,  # Terceira coluna (índice 2)
        13: 4,  # Quinta coluna (índice 4)
        12: 6,  # Sétima coluna (índice 6)
        11: 8   # Nona coluna (índice 8)
    }
    
    try:
        partes = linha_rateio.strip().split('\t')
        valor_str = partes[indices[num_acertos]]
        # Remove 'R$' e converte '.' para '' e ',' para '.' para converter para float
        valor = float(valor_str.replace('R$', '').replace('.', '').replace(',', '.'))
        return valor
    except (IndexError, ValueError):
        return 0.0

def verificar_acertos_combinacao(numeros_jogados, linha_resultado, linha_rateio):
    partes = linha_resultado.strip().split('\t')
    if len(partes) >= 17:
        concurso = partes[0]
        data = partes[1]
        numeros_sorteados = set(int(n) for n in partes[2:])
        
        # Contar quantos números acertou
        acertos = len(numeros_jogados.intersection(numeros_sorteados))
        
        # Se acertou 11 ou mais, retorna os dados do prêmio
        if acertos >= 11:
            valor = obter_valor_premio(linha_rateio, acertos)
            return acertos, (concurso, data, valor)
    return None

def verificar_acertos(numeros_jogados):
    resultados = {
        11: [],  # Lista para guardar (concurso, data, valor) com 11 acertos
        12: [],  # Lista para guardar (concurso, data, valor) com 12 acertos
        13: [],  # Lista para guardar (concurso, data, valor) com 13 acertos
        14: [],  # Lista para guardar (concurso, data, valor) com 14 acertos
        15: []   # Lista para guardar (concurso, data, valor) com 15 acertos
    }
    
    # Se foram jogados mais de 15 números, gerar todas as combinações possíveis
    combinacoes = [set(comb) for comb in itertools.combinations(numeros_jogados, 15)]
    
    # Lista para guardar todos os concursos analisados
    todos_concursos = []
    
    # Ler o arquivo de resultados e rateios simultaneamente
    with open('resultados.txt', 'r') as arquivo_resultados, open('rateio.txt', 'r') as arquivo_rateio:
        for linha_resultado, linha_rateio in zip(arquivo_resultados, arquivo_rateio):
            partes = linha_resultado.strip().split('\t')
            if len(partes) >= 17:
                concurso = partes[0]
                data = partes[1]
                # Guardar informação do concurso
                todos_concursos.append((concurso, data))
                
                # Para cada combinação de 15 números, verificar os acertos
                melhores_acertos = []  # Lista para guardar os melhores resultados deste concurso
                for combinacao in combinacoes:
                    resultado = verificar_acertos_combinacao(combinacao, linha_resultado, linha_rateio)
                    if resultado:
                        melhores_acertos.append(resultado)
                
                # Adicionar apenas o melhor resultado de cada concurso (maior número de acertos)
                if melhores_acertos:
                    melhor = max(melhores_acertos, key=lambda x: x[0])
                    resultados[melhor[0]].append(melhor[1])
    
    return resultados, todos_concursos

def filtrar_resultados_por_ano(resultados, todos_concursos, ano):
    resultados_ano = {
        11: [],
        12: [],
        13: [],
        14: [],
        15: []
    }
    
    # Filtrar concursos do ano
    concursos_do_ano = [(conc, data) for conc, data in todos_concursos 
                        if datetime.strptime(data, '%d/%m/%Y').year == ano]
    
    # Filtrar resultados do ano
    for acertos in resultados:
        for concurso, data, valor in resultados[acertos]:
            data_concurso = datetime.strptime(data, '%d/%m/%Y')
            if data_concurso.year == ano:
                resultados_ano[acertos].append((concurso, data, valor))
    
    return resultados_ano, len(concursos_do_ano)

def mostrar_estatisticas(resultados, titulo, total_concursos=None):
    print(f"\n{titulo}")
    print("-" * 60)
    
    if total_concursos is not None:
        print(f"Total de concursos analisados: {total_concursos}")
        print("-" * 60)
    
    total_premios = 0
    total_valor = 0.0
    
    for acertos in range(15, 10, -1):
        qtd = len(resultados[acertos])
        valor_faixa = sum(valor for _, _, valor in resultados[acertos])
        total_premios += qtd
        total_valor += valor_faixa
        print(f"{acertos} acertos: {qtd:3d} prêmio(s) - Total: R$ {valor_faixa:,.2f}")
    
    if total_premios > 0:
        todos_premios = [(conc, data, valor) 
                        for acertos in range(15, 10, -1)
                        for conc, data, valor in resultados[acertos]]
        
        primeiro_premio = min(todos_premios, key=lambda x: int(x[0]))
        ultimo_premio = max(todos_premios, key=lambda x: int(x[0]))
        
        print(f"\nTotal de prêmios: {total_premios}")
        print(f"Valor total ganho: R$ {total_valor:,.2f}")
        print(f"Primeiro prêmio: Concurso {primeiro_premio[0]} ({primeiro_premio[1]})")
        print(f"Último prêmio: Concurso {ultimo_premio[0]} ({ultimo_premio[1]})")
    else:
        print("\nNenhum prêmio encontrado neste período!")

def mostrar_resumo(resultados, todos_concursos, numeros_jogados):
    print("\n" + "=" * 60)
    print("RESUMO DOS RESULTADOS")
    print("=" * 60)
    
    # Mostrar os números jogados
    numeros_formatados = ", ".join(str(n) for n in sorted(numeros_jogados))
    print(f"\nNúmeros jogados ({len(numeros_jogados)} números): {numeros_formatados}")
    
    if len(numeros_jogados) > 15:
        qtd_combinacoes = len(list(itertools.combinations(numeros_jogados, 15)))
        print(f"\nQuantidade de combinações de 15 números analisadas: {qtd_combinacoes}")
    
    # Mostrar estatísticas gerais
    mostrar_estatisticas(resultados, "Estatísticas Gerais (Todos os períodos)", len(todos_concursos))
    
    # Mostrar estatísticas do ano de 2025
    resultados_2025, total_concursos_2025 = filtrar_resultados_por_ano(resultados, todos_concursos, 2025)
    mostrar_estatisticas(resultados_2025, "\nEstatísticas de 2025", total_concursos_2025)

def main():
    print("\nDigite entre 15 e 20 números (de 1 a 25) separados por espaço:")
    try:
        # Ler entrada do usuário e converter para lista de inteiros
        entrada = input().strip()
        numeros = [int(n) for n in entrada.split()]
        
        # Validar a entrada
        valido, mensagem = validar_entrada(numeros)
        if not valido:
            print(mensagem)
            return
        
        # Verificar acertos
        resultados, todos_concursos = verificar_acertos(numeros)
        
        # Mostrar resultados detalhados
        print("\nResultados encontrados:")
        print("-" * 70)
        
        for acertos in range(15, 10, -1):
            concursos = resultados[acertos]
            if concursos:
                print(f"\n{acertos} acertos ({len(concursos)} ocorrências):")
                for concurso, data, valor in concursos:
                    print(f"Concurso {concurso} ({data}) - Prêmio: R$ {valor:,.2f}")
        
        # Mostrar resumo final
        mostrar_resumo(resultados, todos_concursos, numeros)
            
    except ValueError:
        print("Erro: Digite apenas números separados por espaço!")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")

if __name__ == "__main__":
    main()
