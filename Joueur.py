class Joueur():
    def __init__(self, surnom):
        # On peut imaginer que lors de la création du joueur, ce dernier n'a pas encore de carte.
        self.nom = surnom
        self.nbCartes = 0 # valeur par défaut qui sera modifiée
        self.mainJoueur = []  # valeur par défaut qui sera modifiée
 
    ###########################################################################
    ################# Définition des méthodes d'instances #####################
    ###########################################################################
    def setMain(self,listeCartes):
        ''' Initialise la main du joueur avec la liste des cartes donnée comme paramètre d’entrée '''
        self.mainJoueur = listeCartes
        self.nbCartes= self.nbCartes + len(self.mainJoueur)
 
    def getNom(self):
        '''Accesseur de l’attribut nom '''
        return self.nom
 
    def getNbCartes(self):
        '''Accesseur de l’attribut nbCartes'''
        return self.nbCartes
 
    def jouerCarte(self):
        '''Enlève et renvoie la dernière carte du dessus (objet de type Carte) de la main du joueur,
         ou retourne None s’il n’y a plus de cartes dans la main du joueur'''
        derniereCarte= (self.mainJoueur[-1])
        if (derniereCarte == []):
            print("None")
        else:
            self.mainJoueur.pop()
            self.nbCartes = self.nbCartes - 1
            return derniereCarte
 
    def insererMain(self,listeCartesGagnees):
        ''' Méthode qui insère des cartes dans la main du Joueur « en dessous »'''
        for liste in listeCartesGagnees:
            self.mainJoueur.insert(0,liste)
            self.nbCartes = self.nbCartes +1
        return self.mainJoueur