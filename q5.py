def encontra_palavras(lista_palavras, letra):
    palavras_iniciam_com_letra = []
    for palavra in lista_palavras:
        if palavra.startswith(letra):
            palavras_iniciam_com_letra.append(palavra)
    return palavras_iniciam_com_letra
