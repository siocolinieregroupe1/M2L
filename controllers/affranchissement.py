def saisiAffranchissement():
    rowsAffranchissement=db().select(db.affranchissement.ALL, distinct = True)
    rowsLigue=db().select(db.ligue.ALL, distinct = True)
    return locals()

def ajoutAffranchissement():
    idAffranchissement = request.vars.affranchissement
    Quantite = request.vars.quantiteAffranchissement
    idLigue = request.vars.idLigue
    dateAffranchissement = request.vars.dateAffranchissement


    db.prestation.insert (datePrestation = dateAffranchissement, codeAffranchissement = idAffranchissement, quantite = Quantite, codeLigue = idLigue)

    return locals()
