from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from ebc.nbr2018 import nbr2018MessageFactory as _



class ICadastro(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    midia = schema.TextLine(
        title=_(u"Midia"),
        required=True,
        description=_(u"Field description"),
    )
#
    telefone = schema.TextLine(
        title=_(u"Telefone"),
        required=True,
        description=_(u"Field description"),
    )
#
    email = schema.TextLine(
        title=_(u"Email"),
        required=True,
        description=_(u"Field description"),
    )
#
    nome = schema.TextLine(
        title=_(u"Nome"),
        required=True,
        description=_(u"Field description"),
    )
#
    estado = schema.TextLine(
        title=_(u"Estado"),
        required=True,
        description=_(u"Field description"),
    )
#
    cidade = schema.TextLine(
        title=_(u"Cidade"),
        required=True,
        description=_(u"Field description"),
    )
#
    Empresa = schema.TextLine(
        title=_(u"Empresa"),
        required=True,
        description=_(u"Field description"),
    )
#
