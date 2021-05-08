import os
import shutil

from datetime import datetime
from pprint import pprint


CAMINHO_RAIZ_LEITURA = os.path.join('..', 'palavras-cruas')
CAMINHO_RAIZ_ESCRITA = os.path.join('..', 'palavras-tratadas')
PASTA_JUNTAS = 'juntas'
PASTA_SEPARADAS = 'separadas'
MONOSSILABAS = 'monossilabas'
DISSILABAS = 'dissilabas'
TRISSILABAS = 'trissilabas'
POLISSILABAS = 'polissilabas'


palavras_agrupadas = {}
palavras_agrupadas[MONOSSILABAS] = []
palavras_agrupadas[DISSILABAS] = []
palavras_agrupadas[TRISSILABAS] = []
palavras_agrupadas[POLISSILABAS] = []


def junta_palavras_juntas():
    caminho_arquivos = os.path.join(CAMINHO_RAIZ_LEITURA, PASTA_JUNTAS)
    for classificacao in os.listdir(caminho_arquivos):
        caminho_classificacao = os.path.join(caminho_arquivos, classificacao)
        for arquivo_nome in os.listdir(caminho_classificacao):
            caminho_arquivo = os.path.join(caminho_classificacao, arquivo_nome)
            print(f'Lendo arquivo {caminho_arquivo}')
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                for palavra in arquivo.readlines():
                    if(palavra != '\n'):
                        if palavra.upper() not in palavras_agrupadas[classificacao]:
                            palavras_agrupadas[classificacao].append(palavra.upper())



def junta_palavras_separadas():
    caminho_arquivos = os.path.join(CAMINHO_RAIZ_LEITURA, PASTA_SEPARADAS)
    for arquivo_nome in os.listdir(caminho_arquivos):
        caminho_arquivo = os.path.join(caminho_arquivos, arquivo_nome)
        print(f'Lendo arquivo {caminho_arquivo}')
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            for palavra in arquivo.readlines():
                if(palavra != '\n'):
                    quantidade_tracos = palavra.count('-')
                    palavra = palavra.replace('-', '').upper()
                    if (quantidade_tracos  == 0) and (palavra not in palavras_agrupadas[MONOSSILABAS]):
                        palavras_agrupadas[MONOSSILABAS].append(palavra)
                    elif (quantidade_tracos == 1) and (palavra not in palavras_agrupadas[DISSILABAS]):
                        palavras_agrupadas[DISSILABAS].append(palavra)
                    elif (quantidade_tracos == 2) and (palavra not in palavras_agrupadas[TRISSILABAS]):
                        palavras_agrupadas[TRISSILABAS].append(palavra)
                    elif (quantidade_tracos >= 3) and (palavra not in palavras_agrupadas[POLISSILABAS]):
                        palavras_agrupadas[POLISSILABAS].append(palavra)


def salva_palavras(palavras_dict):
    todas_as_palavras = []
    for classificacao, palavras in palavras_dict.items():
        nome_arquivo = f'{classificacao.upper()}-{len(palavras)}.txt'
        nome_arquivo = os.path.join(CAMINHO_RAIZ_ESCRITA, nome_arquivo)
        print(f'Salvando palavras {classificacao.upper()} em {nome_arquivo}')
        todas_as_palavras += palavras
        with open(nome_arquivo, 'w', encoding='utf-8') as fl:
            for palavra in palavras:
                fl.write(palavra)
    nome_arquivo = f'PALAVRAS-{len(todas_as_palavras)}.txt'
    nome_arquivo = os.path.join(CAMINHO_RAIZ_ESCRITA, nome_arquivo)
    print(f'Salvando totas as palavras em {nome_arquivo}\n')
    with open(nome_arquivo, 'w', encoding='utf-8') as fl:
        for palavra in todas_as_palavras:
            fl.write(palavra)


def remove_arquivos_palavras():
    for arquivo in os.listdir(CAMINHO_RAIZ_ESCRITA):
        os.remove(os.path.join(CAMINHO_RAIZ_ESCRITA, arquivo))


def main():
    print(f'\t\t\t{datetime.now().strftime("%A %d. %B %Y %H:%M:%S")}\n')
    junta_palavras_juntas()
    junta_palavras_separadas()
    print(f'\nTotal de palavras MONOSSILABAS: {len(palavras_agrupadas[MONOSSILABAS])}')
    print(f'Total de palavras DISSILABAS: {len(palavras_agrupadas[DISSILABAS])}')
    print(f'Total de palavras TRISSILABAS: {len(palavras_agrupadas[TRISSILABAS])}')
    print(f'Total de palavras POLISSILABAS: {len(palavras_agrupadas[POLISSILABAS])}\n')
    remove_arquivos_palavras()
    salva_palavras(palavras_agrupadas)


if __name__ == '__main__':
    main()
