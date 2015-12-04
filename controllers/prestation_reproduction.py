# -*- coding: utf-8 -*-
# essayez quelque chose comme

def saisiReproduction():
    rowsLigue=db().select(db.ligue.ALL, distinct = True)
    rowsReproduction=db().select(db.reproduction.ALL, distinct = True)
    rowsAffranchissement=db().select(db.affranchissement.ALL, distinct= True)
    rowsFacture=db().select(db.facture.ALL, distinct= True)
    dir(db)
    
    
    return locals()

def ajoutReproduction():
    datePrestation = request.vars.datePrestation
    quantite = request.vars.quantite
    codeLigue=request.vars.codeLigue
    codeReproduction=request.vars.codeReproduction
    codeAffranchissement=request.vars.codeAffranchissement
    codeFacture=request.vars.codeFacture

    db.prestation.insert( datePrestation =datePrestation, quantite =quantite,codeLigue =codeLigue, codeReproduction =codeReproduction, codeAffranchissement=codeAffranchissement, codeFacture=codeFacture)
    return locals()
