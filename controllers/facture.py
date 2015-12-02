# -*- coding: utf-8 -*-
# essayez quelque chose comme
def index(): return dict(message="hello from facture.py")

@auth.requires_membership('Employe CROSL')
def choixLigue():
    rowsLesLigues = db().select(db.ligue.id,db.ligue.nom)
    return locals()

@auth.requires_membership('Employe CROSL')
def listePrestation():
    idLigue = request.vars.listeLigue #récupère l'identifiant de la ligue
    
    libelleLigue = db(db.ligue.id == idLigue).select(db.ligue.nom)
    listePrestations = db(db.prestation.codeLigue == idLigue and db.prestation.status=='A Payer').select(db.prestation.ALL) #affiche toutes les prestations de la ligue 
    listeRepro = db().select(db.reproduction.ALL)
    listeAffranchissement = db().select(db.affranchissement.ALL)
    return locals()

def creationFacture():
    idLigue = request.vars.codeLigue
    listePrestations = db(db.prestation.codeLigue == idLigue and db.prestation.status=='A Payer').select(db.prestation.id)
    return locals()

def ajoutFacture():
    idLigue = request.vars.codeLigue
    codePrestation = request.vars.codePrestation
    dateEdition = request.vars.dateEdition
    dateEcheance = request.vars.dateEcheance

    db(db.prestation.id==codePrestation).update(status="Facturé")
    db.facture.insert(dateEdition=dateEdition,dateEcheance=dateEcheance,codePrestation=codePrestation)
    return locals()
