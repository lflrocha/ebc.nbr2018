# -*- coding: utf-8 -*-
"""Definition of the Cadastro content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from ebc.nbr2018 import nbr2018MessageFactory as _

from ebc.nbr2018.interfaces import ICadastro
from ebc.nbr2018.config import PROJECTNAME

CadastroSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'midia',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Midia"),
            description=_(u"Field description"),
        ),
        required=True,
    ),


    atapi.StringField(
        'telefone',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Telefone"),
            description=_(u"Field description"),
        ),
        required=True,
    ),


    atapi.StringField(
        'email',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Email"),
            description=_(u"Field description"),
        ),
        required=True,
        validators=('isEmail'),
    ),


    atapi.StringField(
        'nome',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Nome"),
            description=_(u"Field description"),
        ),
        required=True,
    ),


    atapi.StringField(
        'estado',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Estado"),
            description=_(u"Field description"),
        ),
        required=True,
    ),


    atapi.StringField(
        'cidade',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Cidade"),
            description=_(u"Field description"),
        ),
        required=True,
    ),


    atapi.StringField(
        'Empresa',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Empresa"),
            description=_(u"Field description"),
        ),
        required=True,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

CadastroSchema['title'].storage = atapi.AnnotationStorage()
CadastroSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(CadastroSchema, moveDiscussion=False)


class Cadastro(base.ATCTContent):
    """Description of the Example Type"""
    implements(ICadastro)

    meta_type = "Cadastro"
    schema = CadastroSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    midia = atapi.ATFieldProperty('midia')

    telefone = atapi.ATFieldProperty('telefone')

    email = atapi.ATFieldProperty('email')

    nome = atapi.ATFieldProperty('nome')

    estado = atapi.ATFieldProperty('estado')

    cidade = atapi.ATFieldProperty('cidade')

    Empresa = atapi.ATFieldProperty('Empresa')


atapi.registerType(Cadastro, PROJECTNAME)
