# -*- coding: utf-8 -*-
""" Example view
"""

# Zope imports
from Acquisition import aq_inner
from zope.interface import Interface
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.textfield.value import RichTextValue
from DateTime import DateTime
import urllib2
import json
from HTMLParser import HTMLParser

class ItvpView(BrowserView):
    """ Render the title and description of item only (example)
    """

    template = ViewPageTemplateFile('itvp.pt')

    def getVideosItvp(self, rss):
        h = HTMLParser()
        headers = { 'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11' }
        req = urllib2.Request(rss, None, headers)
        f = urllib2.urlopen(req)
        feed = f.read()
        videos = feed.split('<item>')
        vet = []
        for video in videos:

            titulo = ''
            descricao = ''
            link = ''
            data = ''
            linhas = video.split('\n')
            for linha in linhas:
                linha = linha.strip()
                try:
                    if linha.startswith('<title>'):
                        titulo = h.unescape(linha.replace('<title>','').replace('</title>','')).decode('latin-1')
                    elif linha.startswith('<link>'):
                        link = h.unescape(linha.replace('<link>','').replace('</link>',''))
                    elif linha.startswith('<dc:date>'):
                        data = h.unescape(linha.replace('<dc:date>','').replace('</dc:date>',''))
                    elif linha.startswith('<description>'):
                        descricao = h.unescape(linha.replace('<description>','').replace('</description>',''))
                except:
                    pass
            if data:
                vet.append({'titulo': titulo, 'link': link, 'data': data, 'descricao': descricao})
        return vet


    def criaVideos(self):
        """Return a catalog search result of sessions to show."""

        context = aq_inner(self.context)
        rss = "http://200.17.0.2/feed?vspace=65798052&all_vs=false"
        videos = self.getVideosItvp(rss)
        total = 0
        for video in videos:
            titulo = video['titulo']

            descricao = video['descricao']
            data = video['data']
            aux = data.split('T')
            data = aux[0].replace('-','/')
            hora = aux[1]
            hora = hora[:5]
            dt = DateTime(data + ' ' + hora)
            link = video['link']
            id = link.split('?')[1]
            id = id.split('&selected_page')
            id = id[0]
            thumb = "http://df.itvrp.ebc.com.br/thumb?%s&node=EBC-DF&domain=TVBRASIL&selected_page=1&all_vs=false" % id
            ploneId = id.split('contentcode=')
            ploneId = ploneId[1]

            try:
                context.invokeFactory('Video do ITVP', id=ploneId, title=titulo)
                obj = context[ploneId]
                obj.setTitle(titulo)
                obj.setDescricao(descricao)
                obj.setCreationDate(dt)
                obj.setEffectiveDate(dt)
                obj.setModificationDate(dt)
                obj.setThumbnail(ploneId)
                obj.setVideoid(ploneId)
                obj.reindexObject()
                total = total + 1

            except:
                print titulo
        return "%s vídeos importados" % total


    def __call__(self):
        """"""
        self.status = self.criaVideos()
        return self.template()
