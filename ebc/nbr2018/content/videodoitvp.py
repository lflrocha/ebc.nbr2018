# -*- coding: utf-8 -*-
"""Definition of the Video do ITVP content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from ebc.nbr2018 import nbr2018MessageFactory as _

from ebc.nbr2018.interfaces import IVideodoITVP
from ebc.nbr2018.config import PROJECTNAME

VideodoITVPSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

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

VideodoITVPSchema['title'].storage = atapi.AnnotationStorage()
VideodoITVPSchema['description'].storage = atapi.AnnotationStorage()
VideodoITVPSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoITVPSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoITVPSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoITVPSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoITVPSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoITVPSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoITVPSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoITVPSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoITVPSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoITVPSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoITVPSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
VideodoITVPSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(VideodoITVPSchema, moveDiscussion=False)


class VideodoITVP(base.ATCTContent):
    """Description of the Example Type"""
    implements(IVideodoITVP)

    meta_type = "VideodoITVP"
    schema = VideodoITVPSchema
    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    videoid = atapi.ATFieldProperty('videoid')
    thumbnail = atapi.ATFieldProperty('thumbnail')
    descricao = atapi.ATFieldProperty('descricao')

atapi.registerType(VideodoITVP, PROJECTNAME)
