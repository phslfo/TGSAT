from django.conf.urls.defaults import patterns
import settings
#from django.views.static import serve                                           #Necessary @UnusedImport
#from django.conf import settings

urlpatterns = patterns('',
    
    (r'^$', 'views.MainPage'),
    (r'^realtime$', 'realtime.views.realtime'),
    (r'^tp', 'views.tp'),
    
#    (r'^importData', 'coleta.views.import_data'),
#    (r'^resumo', 'coleta.views.resumo'),
#    (r'^consulta', 'coleta.views.consulta'),
    
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #(r'^articles/(\d{4})/$', 'mysite.views.year_archive'),
    #(r'^articles/(\d{4})/(\d{2})/$', 'mysite.views.month_archive'),
    #(r'^articles/(\d{4})/(\d{2})/(\d+)/$', 'mysite.views.article_detail'),
)