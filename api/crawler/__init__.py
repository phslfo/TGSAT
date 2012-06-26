# -*- coding: utf-8 -*-

import urllib
import sys
import re
import json
import string

URL = 'http://www.sentiment140.com/search?query=mib3&hl=en'

def captura_html(url):
    html_data = urllib.urlopen(url).read()
    return html_data

def extrai_sentiment140(html):
    lista = re.search(r'<div id="classifiedTweets">.*</div>', html, re.S)
    rdata = []
    
    if lista:
        opa = re.findall(r'<div class="section(.*?)</div>', lista.group(), re.S)
        
        for t in opa:
            try:
                texto = t[string.find(t, '</a>:') + 6:]
                texto = texto.lower()
                texto = texto.replace('<b>', '')
                texto = texto.replace('</b>', '')
                texto = texto.replace('\n', '')
                texto = texto.replace('\r', '')
                
                sentimento = t[:string.find(t, '"')]
                sentimento = sentimento.replace('negative', 'neg')
                sentimento = sentimento.replace('positive', 'pos')
                
                rdata.append(sentimento.strip() + ' .:. ' + texto.strip())
            except: continue
    
    return rdata

def extrai_socialmention(html):
    lista = re.search(r'<div id="results" (.*?)<div id="column_right">', html, re.S)
    rdata = []
    
    if lista:
        opa = re.findall(r'<div class="result clearfix">\n    (.*?)</h3>', lista.group(), re.S)
        
        for t in opa:
            try:
                sentimento = re.search(r'title="Sentiment: (.*?) (.*?)"', t, re.S).group(2)[1:-1]
                texto = re.search(r'<a (.*?)>(.*?)</a>', t, re.S).group(2)
                texto = texto.lower()
                texto = texto.replace('<b>', '')
                texto = texto.replace('</b>', '')
                texto = texto.replace('\n', '')
                texto = texto.replace('\r', '')
                
                sentimento = sentimento.replace('negative', 'neg')
                sentimento = sentimento.replace('positive', 'pos')
                
                rdata.append(sentimento + " .:. " + texto)                
            except: pass            
    
    return rdata
    
if __name__ == '__main__':
    # html_data = captura_html(URL)
    # status = extrai_socialmention(html_data.read())
    
    import glob
    
    all = []
    for f in glob.glob("*.htm"):
        if f.startswith("140"):
            html_data = open(f, 'r')
            all += extrai_sentiment140(html_data.read())
        else:
            html_data = open(f, 'r')
            all += extrai_socialmention(html_data.read())
            
    print 'Total:', len(all)
    print 'Positivos:', len([line for line in all if line.startswith("pos")])
    print 'Neutros:', len([line for line in all if line.startswith("neutral")])
    print 'Negativos:', len([line for line in all if line.startswith("neg")])
    
    f = open('../training set.txt', 'w')
    for line in all:
        f.write(line + '\n')