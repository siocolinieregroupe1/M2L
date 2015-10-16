# -*- coding: utf-8 -*-
db.define_table('ligue',
             Field('nom','string',requires=IS_NOT_EMPTY()),
             Field('adresseRue','string',requires=IS_NOT_EMPTY()),
             Field('ville','string',requires=IS_NOT_EMPTY()),
             Field('cp','string',requires=IS_NOT_EMPTY()),
             Field('tel','string',requires=IS_NOT_EMPTY()),
             Field('URLSiteWeb','string'),
             Field('emailContact','string')
             ,migrate=False)

db.define_table('facture',
                Field('dateEdition','datetime'),
                Field('dateEcheance', 'datetime'),
                Field('dateReglement', 'datetime')
               ,migrate=False)

db.define_table('relance',
                Field('dateRelance','datetime'),
                Field('numFacture','reference facture', requires=IS_IN_DB(db,db.facture.id))
               ,migrate=False)

db.define_table('affranchissement',
                Field('libelle','string',requires=IS_NOT_EMPTY()),
                Field('coutUnitaire','integer',requires=IS_NOT_EMPTY)
               ,migrate=False)

db.define_table('reproduction',
                Field('libelle','string',requires=IS_NOT_EMPTY()),
                Field('PrixUnitaire','integer',requires=IS_NOT_EMPTY())
               ,migrate=False)

db.define_table('prestation',
                Field('quantite','integer'),
                Field('datePrestation','datetime'),
                Field('codeLigue','reference ligue',requires=IS_IN_DB(db,db.ligue.id)),
                Field('codeFacture','reference facture',requires=IS_IN_DB(db,db.facture.id)),
                Field('codeAffranchissement','reference affranchissement',requires=IS_IN_DB(db,db.affranchissement.id)),
                Field('codeReproduction','reference reproduction',requires=IS_IN_DB(db,db.reproduction.id))
               ,migrate=False)
