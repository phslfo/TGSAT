'''
Created on 13/03/2012

@author: Paulo Oliveira
'''
import util
from coleta import control

def import_data(request):
    a = control.import_from_txt('coleta/data/base.txt')

    return util.request.print_html('Finished' + str(a))

def resumo(request):
    return util.request.print_html(control.resumo())

def consulta(request):
    
    from coleta.models import Tweet
    
    retorno = ''
    t = Tweet.all()
    t.filter('author_location =', 'San Francisco')
    for a in t:
        retorno += str(a.text) + ' <br /> '
    return util.request.print_html( str(retorno) )
    