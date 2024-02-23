class Bataille():
    def __init__(self, nomJ1, nomJ2, tailleJeuCartes):
        # L'initialisation va créer les 2 joueurs, mélanger et distribuer les cartes
        self.J1 = joueur(nomJ1)
        self.J2 = joueur(nomJ2) # valeur par défaut qui sera modifiée
        self.jeuCartes = JeuCartes(tailleJeuCartes) # valeur par défaut qui sera modifiée
        ## On mélange le jeu et on le distribue aux 2 joueurs


    ###########################################################################
    ################# Définition des méthodes d'instances #####################
    ###########################################################################
    def jouer(self):
        ''' Chaque joueur pose une carte. On regarde qui gagne. Ce dernier remporte les cartes.
        En cas d'égalité, chacun reprend sa carte (<- Ici, on peut changer la règle)
        '''
        toto=Joueur("Toto")
        dupont=Joueur("Dupont")
        print("La carte du joueur", toto.getNom()," est :",toto.getNbCartes())
        print("La carte du joueur", dupont.getNom()," est :",dupont.getNbCartes())
        if (Joueur(toto.getNbCartes())<dupont.getNbCartes()):
            print(dupont.getNom()," a gagné. Nombre de carte du joueur:",dupont.getNbCartes())
            if (Joueur(toto.getNbCartes())>dupont.getNbCartes()):
                print(toto.getNom()," a gagné. Nombre de carte du joueur:",toto.getNbCartes())
        print(toto.getNom()," a gagné. Nombre de carte du joueur:",toto.getNbCartes())

