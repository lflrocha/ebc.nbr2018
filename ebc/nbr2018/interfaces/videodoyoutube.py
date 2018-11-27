from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from ebc.nbr2018 import nbr2018MessageFactory as _



class IVideodoyoutube(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    videoid = schema.TextLine(
        title=_(u"Video ID"),
        required=True,
        description=_(u"Field description"),
    )
#
    thumbnail = schema.TextLine(
        title=_(u"Thumbnail"),
        required=False,
        description=_(u"Field description"),
    )
#
    descricao = schema.Text(
        title=_(u"Descricao"),
        required=False,
        description=_(u"Field description"),
    )
#
