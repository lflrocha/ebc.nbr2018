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
import urllib
import json

class YoutubeView(BrowserView):
    """ Render the title and description of item only (example)
    """

    template = ViewPageTemplateFile('youtube.pt')

    def get_all_video_in_channel(self, channel_id):
        api_key = "XXXX"

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
        first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

        video_links = []
        url = first_url
        z = 0
        while z < 10:
            z = z + 1
            inp = urllib.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    metadados =  [i['snippet']['title'], i['snippet']['description'], i['snippet']['publishedAt'], i['snippet']['thumbnails']['high']['url'] , base_video_url + i['id']['videoId']]
                    video_links.append(metadados)

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except:
                break
        return video_links


    def criaVideos(self):
        """Return a catalog search result of sessions to show."""

        context = aq_inner(self.context)

        videos = self.get_all_video_in_channel('UCjaWLFTNqLkq3ZY2BJ4NYRg')
        total = 0
        for video in videos:
            titulo = video[0]
            descricao = video[1]
            aux = video[2].split('T')
            data = aux[0].replace('-','/')
            hora = aux[1].replace('-02:00','')
            hora = hora [:5]
            dt = DateTime(data + ' ' + hora)
            thumb = video[3]
            link = video[4]
            id = link.split('?v=')[1]
            ploneId = id.replace('_','-')

            try:
                context.invokeFactory('Video do youtube', id=ploneId, title=titulo)
                obj = context[ploneId]
                obj.setTitle(titulo)
                obj.setDescricao(descricao)
                obj.setCreationDate(dt)
                obj.setEffectiveDate(dt)
                obj.setModificationDate(dt)
                obj.setThumbnail(thumb)
                obj.setVideoid(id)
                obj.reindexObject()
                total = total + 1

            except:
                pass
        return "%s vídeos importados" % total


    def __call__(self):
        """"""
        self.status = self.criaVideos()
        return self.template()
