#coding=UTF-8

'''
                                        DECORATORS
'''

import functools 
from django.http import HttpRequest

def check_is_not_logged(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            request = None
            for x in args:
                if isinstance(x, HttpRequest):
                    request = x
                    break
            if not request:
                for k in kwargs:
                    if isinstance(kwargs[k], HttpRequest):
                        request = kwargs[k]
                        break 
            
            if request.session.has_key('type'): #Is Logged
                return request.redirect_to('/usuario') 
            else:
                return func(*args, **kwargs)
                
        return wrapper

def check_is_logged(value):
    ''' 
         0 - Users
         1 - Doctors and Attendants and Dentists
    '''
    def factory(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            request = None
            for x in args:
                if isinstance(x, HttpRequest):
                    request = x
                    break
            if not request:
                for k in kwargs:
                    if isinstance(kwargs[k], HttpRequest):
                        request = kwargs[k]
                        break 
            
            type = request.session.get('type', None)
            
            if type:
                return func(*args, **kwargs)
            else:
                if value == 0:
                    request.session['agendamento'] = '/agendamento?' + str(request.META['QUERY_STRING'])
                    return request.render('user/logar-ou-cadastrar.xhtml', {}, request)
                elif value == 1:
                    return request.render('base/login.xhtml', {}, request)
        return wrapper   
    return factory

def check_is_some_roles(func, roles, error_message):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        request = None
        for x in args:
            if isinstance(x, HttpRequest):
                request = x
                break
        if not request:
            for k in kwargs:
                if isinstance(kwargs[k], HttpRequest):
                    request = kwargs[k]
                    break 
        
        type = request.session.get('type')
        if type in roles:
            return func(*args, **kwargs)
        else:
            d = {}
            d['confirmation'] = {
                 'status'  : 'OK',
                 'title'   : 'Ocorreu um erro',
                 'message' : error_message
                 }
            return request.render('base/erro.xhtml', d, request)
    return new_func

#def check_is_user(func):
#    return check_is_some_roles(func, [login_control.LOGIN_TYPE_USER], 'Desculpe, você não está logado como usuário.')
#
#def check_is_doctor(func):
##    return check_is_some_roles(func, [login_control.LOGIN_TYPE_DOCTOR], 'Desculpe, você não está logado como dentista.')            
#    return check_is_some_roles(func, [login_control.LOGIN_TYPE_DENTIST], 'Desculpe, você não está logado como dentista.')            
#
#def check_is_attendant(func):
#    return check_is_some_roles(func, [login_control.LOGIN_TYPE_ATTENDANT], 'Desculpe, você não está logado como atendente.')
#
#def check_is_attendant_or_doctor(func):
#    return check_is_some_roles(func, [login_control.LOGIN_TYPE_ATTENDANT, login_control.LOGIN_TYPE_DOCTOR, login_control.LOGIN_TYPE_DENTIST], 'Desculpe, apenas dentistas e atendentes \n tem acesso a esta página.')

