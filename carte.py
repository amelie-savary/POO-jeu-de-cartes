# Variables globales
couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')
noms = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
valeurs = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Valet':11, 'Dame':12, 'Roi':13, 'As': 14}

# Classe Carte
class Carte:
    def __init__(self, nom, couleur):
        # Affectation des attributs nom et couleur avec contrôle.
        if nom in noms:
            self.nom = nom
        else:
            print ("Le nom est invalide")
        if couleur in couleurs:
            self.couleur = couleur
        else:
            print ("La couleur de la carte est incorrect:")
        self.valeur = valeurs[nom]


########### Définition des méthodes d'instances avec contrôles. ###########
    def setNom(self, new_nom):
        if new_nom in noms:
            self.nom = new_nom
            self.valeur = valeurs[self.new_nom]
        else:
            print ("Le nom est invalide:", self.nom)

    def getNom(self):
        return self.nom

    def getCouleur(self):
        return self.couleur

    def getValeur(self):
        return self.valeur

###############################################

    def egalite(self, carte):
        '''Renvoie True si les cartes ont la même valeur, False sinon
        carte: Objet de type Carte     '''
        if self.getValeur() == carte.getValeur():
            return True
        else:
            return False

    def estSuperieurA(self, carte):
        '''Renvoie True si la valeur de self est supérieur à celle de carte, False sinon
        carte: Objet de type Carte     '''
        if self.getValeur() > carte.getValeur():
            return True
        else:
            return False

    def estInferieurA(self, carte):
        '''Renvoie True si la valeur de self est inférieur à celle de carte, False sinon
        carte: Objet de type Carte     '''
        if self.getValeur() < carte.getValeur():
            return True
        else:
            return False

########## Tests carte. ############

def testCarte():
    valetCoeur = Carte('Valet', 'COEUR')
    print ('Nom:', valetCoeur.getNom())
    print('Couleur:', valetCoeur.getCouleur())
    print('Valeur:', valetCoeur.getValeur())
    valetCoeur.setNom('Dame')
    print('Nom modifié:', valetCoeur.getNom())
    print('Valeur modifié:', valetCoeur.getValeur())

# Essaie des exption: cette instruction conduit à une erreur #
#dameCarreau = Carte('Dame', 'COooEUR')