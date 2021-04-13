import os
import re


ROOT_PATH = '../palavras-cruas/'


def junta_files_palavras_polissilabas():
    path = os.path.join(ROOT_PATH, 'juntas/polissilabas')
    for item in os.listdir(path):
        print(item)


def junta_files_palavras_trissilabas():
    path = os.path.join(ROOT_PATH, 'juntas/trissilabas')
    for item in os.listdir(path):
        print(item)


def junta_files_palavras_dissilabas():
    path = os.path.join(ROOT_PATH, 'juntas/dissilabas')
    for item in os.listdir(path):
        print(item)


def junta_files_palavras_monossilabas():
    monossilabas = []
    path = os.path.join(ROOT_PATH, 'juntas/monossilabas')
    print('Juntando arquivos com palavras monossilabas...')
    for item in os.listdir(path):
        print(f'Monossilabas, file: {item}')
        if not item.startswith('.'):
            file_path = os.path.join(path, item)
            with open(file_path, 'r') as fl:
                for palavra in fl.readlines():
                    monossilabas.append(palavra.replace('\n', ''))
    print('Junção de arquivos de palavras monossilabas concluido')
    return monossilabas
        


def main():
    junta_files_palavras_monossilabas()
    junta_files_palavras_dissilabas()
    junta_files_palavras_trissilabas()
    junta_files_palavras_polissilabas()


if __name__ == "__main__":
    main()
