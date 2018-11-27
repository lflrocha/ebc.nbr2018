# -*- coding: utf-8 -*-
"""Definition of the Video do youtube content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from ebc.nbr2018 import nbr2018MessageFactory as _

from ebc.nbr2018.interfaces import IVideodoyoutube
from ebc.nbr2018.config import PROJECTNAME

VideodoyoutubeSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.StringField(
        'videoid',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Vídeo ID"),
        ),
        required=True,
    ),

    atapi.TextField(
        'descricao',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Descrição"),
        ),
    ),

    atapi.StringField(
        'thumbnail',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Thumbnail"),
        ),
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

VideodoyoutubeSchema['title'].storage = atapi.AnnotationStorage()
VideodoyoutubeSchema['description'].storage = atapi.AnnotationStorage()
VideodoyoutubeSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoyoutubeSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoyoutubeSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoyoutubeSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoyoutubeSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoyoutubeSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoyoutubeSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoyoutubeSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoyoutubeSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoyoutubeSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoyoutubeSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(VideodoyoutubeSchema, moveDiscussion=False)


class Videodoyoutube(base.ATCTContent):
    """Description of the Example Type"""
    implements(IVideodoyoutube)

    meta_type = "Videodoyoutube"
    schema = VideodoyoutubeSchema
    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    videoid = atapi.ATFieldProperty('videoid')
    thumbnail = atapi.ATFieldProperty('thumbnail')
    descricao = atapi.ATFieldProperty('descricao')

atapi.registerType(Videodoyoutube, PROJECTNAME)
