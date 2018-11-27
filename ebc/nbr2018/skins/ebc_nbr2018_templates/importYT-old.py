## Script (Python) "setStatusNbrInfoweb"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

from Products.PythonScripts.Utility import allow_module

allow_module('json')

import urllib
import json
from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFCore.utils import getToolByName

def get_all_video_in_channel(channel_id):
    api_key = "AIzaSyCjIRBLiFccN4ydK_iUebO8B2EmX4FdnOk"

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    z = 0
    while z < 10:
        z = z + 1
        inp = urllib.urlopen(url)
#        print inp
        resp = json.load(inp)
#        print resp

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

a = get_all_video_in_channel('UCjaWLFTNqLkq3ZY2BJ4NYRg')

workflowTool = getToolByName(context, 'portal_workflow')
folder_path = "/".join(context.getPhysicalPath())

return context


#for solicitacao in solicitacoes:
#    obj = solicitacao.getObject()
#    status = workflowTool.getInfoFor(obj, 'review_state')
#    if status in ['finalizado','gerando']:
#        workflowTool.doActionFor(obj, 'retornar')

#context.plone_utils.addPortalMessage(_(u'Infografias solicitadas.'))
#return context.REQUEST.response.redirect(context.absolute_url())
