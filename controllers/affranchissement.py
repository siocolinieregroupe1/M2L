@auth.requires_membership('Employe CROSL')
def Affranchissement():
    return locals()

@auth.requires_membership('Employe CROSL')
def saisiAffranchissement():
    rowsAffranchissement=db().select(db.affranchissement.ALL, distinct = True)
    rowsLigue=db().select(db.ligue.ALL, distinct = True)
    return locals()

@auth.requires_membership('Employe CROSL')
def ajoutAffranchissement():
    idAffranchissement = request.vars.affranchissement
    Quantite = request.vars.quantiteAffranchissement
    idLigue = request.vars.idLigue
    dateAffranchissement = request.vars.dateAffranchissement


    db.prestation.insert (datePrestation = dateAffranchissement, codeAffranchissement = idAffranchissement, quantite = Quantite, codeLigue = idLigue)

    return locals()

@auth.requires_membership('Employe CROSL')
def modifierAffranchissement():
    rowsAffranchissement2=db().select(db.affranchissement.ALL, distinct = True)
    
    return locals()

def modificationFaite():
    idAffranchissement = request.vars.affranchissement
    coutAffranchissement = request.vars.coutAffranchissement

    db(db.affranchissement.id == idAffranchissement).update( coutUnitaire = coutAffranchissement)
    
    return locals()
