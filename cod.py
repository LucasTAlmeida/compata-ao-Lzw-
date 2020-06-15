def compress(uncompressed):
    """Comprimir cacracteres para codigos"""

    # aqui é construido o dicionario
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    #  iniciado primeiro valor vazio do inicio da palavra

    w = ""
    result = []
    #inicia a compressao
    for c in uncompressed:
        wc = w + c
        # faz o proximo caracter raiz ser a prox
        if wc in dictionary:
            w = wc
        #se nao tiver adiciona no dicionario
        else:
            result.append(dictionary[w])
            # adiciona wc no dicionario.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # saida do codigo w.
    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed):
    """descomprime uma lista ks para uma string."""
    from io import StringIO

    # dicionario construido
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))


    # usa StringIO, caso contrario O(N^2)
    # devido à concatenação de strings em um loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    #verifica se tem a condiçao no dict
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        # add w+entry[0] para o dicionario.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()


# Entrada de caracteres a ser comprimidos
compressed = compress('^WED^WE^WEE^WEB^WET')
print('O codigo comprimido foi: ', compressed)
decompressed = decompress(compressed)
print('Descompressão do codigo comprimido: ', decompressed)