#coding=UTF-8

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
import logging

def session(request):
    from django.db.models.query import QuerySet
    
    clear = request.GET.get('clear', None)
    if clear == 'yes':
        request.session.clear()
        return print_html('sessao limpa!')
    
    try:            
        a_str = ''
        for a in request.session.keys():
            obj = request.session[a]
            if type(obj) == QuerySet:
                a_str = a_str + str(a) + ': ' + str(['<br/>' + str(o) for o in obj.values()]) + '<br /> <br />'
            else:
                a_str = a_str + str(a) + ': ' + str(obj) + '<br /> <br />'
        
        return print_html(a_str)
    except:
        return print_html('Exception: (request.py - session())')
    
def print_logging(x):
    logging.info(str(x))
    
def print_html(x):
    return HttpResponse(x)
    
def render(template, d = {}, request = None):
    return render_to_response(template, d)

def redirect_to(url):
    return redirect(url)


##coding=UTF-8
#
#from google.appengine.ext import webapp
#from google.appengine.ext.webapp import template
#
#import wsgiref
#import os
#
#class BasePage(webapp.RequestHandler):
#    def initialize(self, request, response):
#        webapp.RequestHandler.initialize(self, request, response)
#    
#    def render(self, url, d = {}):
#        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), url)
#        self.response.headers['Content-Type'] = 'text/html;charset=UTF-8'
#        
#        d['base_url'] = self.getBaseURL()
#        self.response.out.write(template.render(path, d))         
#        
#    def getBaseURL(self):
#        '''
#        o self eh o objeto da requisição da BasePage (RequestHandler)
#        e voce precisa da requisicao pra saber onde o aplicativo esta hospedado
#        '''
##    self.request.headers.get('host', 'no host')        #Imprimir localhost:8080
##    wsgiref.util.request_uri(self.request.environ)     #Retorna http://localhost:8080/possivelerro
##    
##    http://docs.python.org/library/wsgiref.html#wsgiref.util.application_uri
##    retorna do http ate' antes do / depois da porta 
#        base = wsgiref.util.application_uri(self.request.environ)
#        if base.endswith('/'):
#            base = base[:-1] #remove o /
#        return base
#    
#    def println(self, s):
#        return self.response.out.write(str(s) + '<br />')