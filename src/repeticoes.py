import os

RAIZ = '../palavras-tratadas'

def verifica_repeticoes(caminho):
    palavras = []
    with open(caminho, 'r', encoding='utf-8') as fl:
        for palavra in fl.readlines():
            if palavra not in palavras:
                palavras.append(palavra)
            else:
                print(f'Palavra repetida: {palavra}')


def main():
    for arquivo in os.listdir(RAIZ):
        caminho_arquivo = os.path.join(RAIZ, arquivo)
        print(f'Arquivo: {caminho_arquivo}')
        verifica_repeticoes(caminho_arquivo)


if __name__ == "__main__":
    main()
                