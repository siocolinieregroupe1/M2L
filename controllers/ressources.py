# -*- coding: utf-8 -*-
# essayez quelque chose comme
def index(): return dict(message="hello from ressources.py")

def choixAjoutModSup():
    return locals()

def ajouterRessource():
    return locals()

def ajouterRessource2():
    session.typeRessource = request.vars.typeRessource
    session.libelle = request.vars.libelle
    session.cout = request.vars.cout
    if (session.typeRessource == "reproduction"):
        db.reproduction.insert(libelle = session.libelle, PrixUnitaire = session.cout)
    else :
        db.affranchissement.insert(libelle = session.libelle, coutUnitaire = session.cout)
    return locals()

def modifierRessource():
    return locals()

def modifierRessource2() :
    session.TypeRessource4 = request.vars.typeRessource1
    if (session.TypeRessource4 == "reproduction"):
        rowsRessource=db().select(db.reproduction.ALL)
    else:
        rowsRessource=db().select(db.affranchissement.ALL)
    return locals()

def modifierRessource3():
    session.LibelleRessource = request.vars.choixRessourceSupp1
    return locals()

def modifierRessource4():
    session.libelle = request.vars.libelle1
    session.cout = request.vars.cout1
    if (session.TypeRessource4 == "reproduction"):
        db(db.reproduction.libelle == session.LibelleRessource).update(libelle = session.libelle, PrixUnitaire = session.cout)
    else:
        db(db.affranchissement.libelle == session.LibelleRessource).update(libelle = session.libelle, coutUnitaire = session.cout)
    return locals()

def supprimerRessource():
    return locals()

def supprimerRessource2():
    session.TypeRessource1 = request.vars.typeRessource
    if (session.TypeRessource1 == "reproduction"):
        rowsRessource=db().select(db.reproduction.ALL)
    else:
        rowsRessource=db().select(db.affranchissement.ALL)
    return locals()

def supprimerRessource3():
    session.ressourceSupp = request.vars.choixRessourceSupp
    if (session.TypeRessource1 == "reproduction"):
        db(db.reproduction.libelle == session.ressourceSupp).delete()
    else:
        db(db.affranchissement.libelle == session.ressourceSupp).delete()
    return locals()
