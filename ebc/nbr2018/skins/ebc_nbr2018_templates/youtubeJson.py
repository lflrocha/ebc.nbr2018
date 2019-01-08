## Script (Python) "youtubeJson.py"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

import json
from Products.CMFCore.utils import getToolByName
from Products.PythonScripts.Utility import allow_module
allow_module('json')

pc = getToolByName(self, 'portal_catalog')
videos = pc.searchResults(meta_type="Videodoyoutube", review_state="published", sort_on='created', sort_order='reverse')
vet = []
for item in videos:
    obj = item.getObject()
    titulo = item.Title()
    descricao = obj.getDescricao()
    data = obj.effectiveDate()
    videoid = obj.getVideoid()
    vet.append({"titulo": titulo, "descricao": descricao, "data": data, "videoid": videoid})
aux = json.dumps({"videos":vet})
return aux
