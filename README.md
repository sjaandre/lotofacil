# Análise Lotofácil

Este projeto contém scripts Python para análise de resultados da Lotofácil.

## Funcionalidades

- `lista_mais_sairam.py`: Script que analisa o arquivo de resultados e mostra os números que mais foram sorteados, em ordem decrescente de frequência.

## Como usar

1. Certifique-se de ter um arquivo `resultados.txt` com os resultados da Lotofácil no formato:
   ```
   concurso    data    num1    num2    num3    ...    num15
   ```

2. Execute o script:
   ```
   python lista_mais_sairam.py
   ```

3. O script mostrará uma tabela com os números ordenados por frequência de aparição.

## Requisitos

- Python 3.x 