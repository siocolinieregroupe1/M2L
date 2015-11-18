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
    listePrestations = db(db.prestation.codeLigue == idLigue and db.prestation.status=='A Payer').select(db.prestation.ALL) #affiche toutes les prestations de la ligue 
    listeRepro = db().select(db.reproduction.ALL)
    listeAffranchissement = db().select(db.affranchissement.ALL)
    return locals()
