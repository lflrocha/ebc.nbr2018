# -*- coding: utf-8 -*-
"""Definition of the Capa content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget

# -*- Message Factory Imported Here -*-
from ebc.nbr2018 import nbr2018MessageFactory as _

from ebc.nbr2018.interfaces import ICapa
from ebc.nbr2018.config import PROJECTNAME
from DateTime import DateTime

CapaSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'manchete',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Manchete"),
            description=_(u"Escreva a manchete"),
            maxlength=90
        ),
        required=True,
    ),


    atapi.ReferenceField(
        'conteudo',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Conteúdo"),
            description=_(u"Selecione o conteudo"),
        ),
        required=True,
        relationship='capa_conteudo',
        allowed_types=('Video do youtube'), # specify portal type names here ('Example Type',)
        multiValued=False,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

CapaSchema['title'].storage = atapi.AnnotationStorage()
CapaSchema['description'].storage = atapi.AnnotationStorage()
CapaSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
CapaSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
CapaSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
CapaSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
CapaSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
CapaSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
CapaSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
CapaSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
CapaSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
CapaSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
CapaSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}



schemata.finalizeATCTSchema(CapaSchema, moveDiscussion=False)


class Capa(base.ATCTContent):
    """Description of the Example Type"""
    implements(ICapa)

    meta_type = "Capa"
    schema = CapaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    manchete = atapi.ATFieldProperty('manchete')

    conteudo = atapi.ATReferenceFieldProperty('conteudo')

    def getData(self):
        aux = self.getConteudo()
        data = DateTime(aux.created()).strftime('%d/%m/%Y - %H:%M')
        return data

    def getThumb(self):
        aux = self.getConteudo()
        videoId = aux.getVideoid()
        thumb = "https://img.youtube.com/vi/%s/maxresdefault.jpg" % videoId
        return thumb

    def getLink(self):
        aux = self.getConteudo()
        link = aux.absolute_url()
        return link


atapi.registerType(Capa, PROJECTNAME)
