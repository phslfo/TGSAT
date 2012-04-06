#coding=UTF-8

import request, decorators, json

from unicodedata import normalize

def remover_acentos(txt, codif='utf-8'):
    ''' 
        Devolve cópia de uma str substituindo os caracteres 
        acentuados pelos seus equivalentes não acentuados.
    
        ATENÇÃO: carateres gráficos não ASCII e não alfa-numéricos,
        tais como bullets, travessões, aspas assimétricas, etc. 
        são simplesmente removidos! 
    '''
    
    try:
        return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')
    except Exception:
        #request.print_logging('Remove Acentos: ' + txt)
        return None