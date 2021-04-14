import os
import re

from pprint import pprint


CAMINHO_RAIZ_LEITURA = '../palavras-cruas/'
CAMINHO_RAIZ_ESCRITA = '../palavras-tratadas/'
PASTA_JUNTAS = 'juntas'

    
def junta_palavras_juntas():
    palavras_agrupadas = {}
    caminho_classificacoes = os.path.join(CAMINHO_RAIZ_LEITURA, PASTA_JUNTAS)
    for classificacao in os.listdir(caminho_classificacoes):
        palavras_agrupadas[classificacao] = []
        print(f'Juntando arquivos com palavras {classificacao}...')
        caminho_classificacao = os.path.join(caminho_classificacoes, classificacao)
        for arquivo in os.listdir(caminho_classificacao):
            if not arquivo.startswith('.'):
                caminho_arquivo = os.path.join(caminho_classificacao, arquivo)
                print(f'{classificacao}, arquivo: {caminho_arquivo}')
                with open(caminho_arquivo, 'r') as fl:
                    for palavra in fl.readlines():
                        if palavra not in palavras_agrupadas[classificacao]:
                            palavras_agrupadas[classificacao].append(palavra)
    return palavras_agrupadas


def salva_palavras(palavras_dict):
    todas_as_palavras = []
    for classificacao, palavras in palavras_dict.items():
        print(f'Salvando palavras {classificacao}...')
        nome_arquivo = f'{classificacao.upper()}-{len(palavras)}.txt'
        nome_arquivo = os.path.join(CAMINHO_RAIZ_ESCRITA, nome_arquivo)
        todas_as_palavras += palavras
        with open(nome_arquivo, 'w') as fl:
            for palavra in palavras:
                fl.write(palavra)

    nome_arquivo = f'PALAVRAS-{len(todas_as_palavras)}.txt'
    nome_arquivo = os.path.join(CAMINHO_RAIZ_ESCRITA, nome_arquivo)
    with open(nome_arquivo, 'w') as fl:
        for palavra in todas_as_palavras:
            fl.write(palavra)


def main():
    palavras = junta_palavras_juntas()
    salva_palavras(palavras)


if __name__ == "__main__":
    main()
