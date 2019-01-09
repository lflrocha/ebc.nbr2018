# -*- coding: utf-8 -*-
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
from Products.CMFCore.utils import getToolByName


class YoutubeJsonView(BrowserView):
    """ Render the title and description of item only (example)
    """

    template = ViewPageTemplateFile('youtubeJson.pt')

    def getYoutubeJson(self):
        pc = getToolByName(self, 'portal_catalog')
        videos = pc.searchResults(meta_type="Videodoyoutube", review_state="published", sort_on='created', sort_order='reverse')
        vet = []
        for item in videos:
            obj = item.getObject()
            titulo = item.Title
            descricao = obj.getDescricao()
            data = item.EffectiveDate
            videoid = obj.getVideoid()
            vet.append({"titulo": titulo, "descricao": descricao, "data": data, "videoid": videoid})
        aux = json.dumps({"videos":vet})
        return aux


    def __call__(self):
        """"""
        self.status = self.getYoutubeJson()
        return self.status
