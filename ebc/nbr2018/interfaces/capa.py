from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from ebc.nbr2018 import nbr2018MessageFactory as _



class ICapa(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    manchete = schema.TextLine(
        title=_(u"Manchete"),
        required=True,
        description=_(u"Field description"),
    )
#
    conteudo = schema.Object(
        title=_(u"Conteudo"),
        required=True,
        description=_(u"Field description"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
