#coding=UTF-8

import request, decorators, json

from unicodedata import normalize

def removeNonAscii(s): 
    return "".join(i for i in s if ord(i)<128)

def remover_acentos(txt, codif='utf-8'):
    ''' 
        Devolve copia de uma str substituindo os caracteres 
        acentuados pelos seus equivalentes nao acentuados.
    
        ATENCAO: carateres graficos nao ASCII e nao alfa-numericos,
        tais como bullets, travessoes, aspas assimetricas, etc. 
        sao simplesmente removidos! 
    '''
    
    try:
        txt = removeNonAscii(txt)
        return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')
    except Exception:
        #request.print_logging('Remove Acentos: ' + txt)
        return txt
