#coding=UTF-8

from unicodedata import normalize
from string import punctuation

def remover_acentos(txt, codif='utf-8'):
    ''' 
        Devolve copia de uma str substituindo os caracteres 
        acentuados pelos seus equivalentes nao acentuados.
    
        ATENCAO: carateres graficos nao ASCII e nao alfa-numericos,
        tais como bullets, travessoes, aspas assimetricas, etc. 
        sao simplesmente removidos! 
    '''
    
    try:
        return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')
    except Exception:
        #request.print_logging('Remove Acentos: ' + txt)
        return None

texto = u"@faithsone ㅋㅋㅋ u so smart & progressive. i thou'ght u were like @moontoseu or rick santorum ^^;"

print remover_acentos(texto, "utf-8")
