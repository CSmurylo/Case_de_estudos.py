'''
  Nesse código, é lido o total de palavras em um arquivo .txt e selecionadas as palavras únicas.
  Para usar ele, tem que exportar um arquivo .txt para alguma página e mudar o nome na linha 55 para o arquivo que quer pesquisar.
  Usei o site 'replit.com' para ver como fica no terminal.
  Estudos de BIG-DATA
'''

import os
from collections import defaultdict

def mapear_arquivo(nome_arquivo):
    pares = []
    if not os.path.exists(nome_arquivo):
        raise FileNotFoundError(f"Arquivo {nome_arquivo} não encontrado.")

    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            # Remove espaços extras e converte para minusculas
            linha = linha.strip().lower()
            # Divide a linha em palavras
            palavras = linha.split()
            for palavra in palavras:
                # Remove pontuação simples
                palavra = palavra.strip(',.!?;:''[]{}')
                if palavra: # Verifica se a palavra não está vazia
                    pares.append((palavra, 1))
    return pares


#--------------- ETAPA 2: shuffle ---------------------
def embaralhar(pares):
    """
    Agrupar todas as contagens pela palavra.
    Recebe uma lista de pares (palavra, 1) e retorna um dicionário:
    {palavra: [1,1,1,...]}
    """
    agrupado = defaultdict(list)
    for chave, valor in pares:
        agrupado[chave].append(valor)
    return agrupado


#--------------- ETAPA 3: reduce ---------------------
def reduzir(agrupado):
    """
    Soma os valores de cada palavra.
    Retorna um dicionário { palavra: total_contagem }
    """
    resultado = {}
    for chave, valores in agrupado.items():
        resultado[chave] = sum(valores)
    return resultado


#--------------- Função principal ---------------------
def main():
    nome_arquivo = 'LivroRedesdeComputadores.txt'

    # map
    pares = mapear_arquivo(nome_arquivo)
    print(f"Map concluído: {len(pares)} pares gerados.")
    print("-------------------------------------------")

    # shuffle
    agrupado = embaralhar(pares)
    print(f"Shuffle concluído: {len(agrupado)} palavras únicas.")
    print("-------------------------------------------")

    # reduce
    resultado = reduzir(agrupado)
    print(f"Reduce concluído: {len(resultado)} palavras com contagem total.")
    print("-------------------------------------------")

    # Mostrar as 10 palavras mais frequentes
    palavras_ordenadas = sorted(resultado.items(), key=lambda x: x[1], reverse=True)
    for palavra, contagem in palavras_ordenadas[:10]:
        print(f"{palavra} - {contagem}")
        

if __name__ == "__main__":
    main()
