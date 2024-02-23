from carte import *
import random


# Classe dérivant de la classe Exception et permettant de gérer une exception si on distribue trop de cartes
class TropDeCartesDistribuees(Exception):
  '''Pas assez de cartes dans le jeu. Le nombre de cartes à distribuer est de'''
  pass

        ###################################
      #######################################
    #### Définition de la classe JeuCartes ####
      #######################################
        ###################################

class JeuCartes():

  def __init__(self, nbCartes=52):
    # Le jeu doit comporter 32 ou 52 cartes, ce que vérifie la méthode setNbCartes()
    if nbCartes != 32 or nbCartes != 52:
        nbCartes = 52
    else:
        self.tailleJeu = nbCartes
    # self.jeu est une liste des self.nbCartes
    self.jeu = []
    # On crée un jeu
    self.creerJeu
    # self.indexNextCarte est l'index dans self.jeu de la prochaine carte à distribuer. On distribue d'abord la dernière carte de la liste
    self.indexNextCarte = nbCartes - 1



  ###########################################################################
  ################# Définition des méthodes d'instances #####################
  ###########################################################################
  def getTailleJeu(self):
    ''' Fonction qui retourne le nombre de cartes du jeu

    Valeur retournée: type int
    '''
    print ("Taille jeu :", self.nbCartes)


  def creerJeu(self):
    ''' Cette méthode créée la liste des cartes du champ self.jeu

    '''
    for couleur in couleurs:
        for nom in noms:
            if (self.nbCartes == 32 and nom not in ['2','3','4','5','6']):
                self.jeu.append(Carte(nom, couleur))
            if (self.nbCartes == 52 and nom not in ['2','3','4','5','6']):
                self.jeu.append(Carte(nom, couleur))


  def getJeu(self):
    ''' Cette méthode retourne la liste des cartes correspondant au champ self.jeu
    '''
    return self.jeu


  def melanger(self):
    ''' Cette fonction mélange sur place les cartes de la liste des cartes associée au champ self.jeu
    '''
    return random.shuffle(self.jeu)


  def distribuerCarte(self):
    ''' Cette fonction permet de distribuer une carte à un joueur.
        Elle retourne la carte distribuée et décrémente l'index self.indexNextCarte
        Valeur retournée: Objet de type Carte
    '''
    # On récupère la carte à distribuer
    carte = self.indexNextCarte
    # On décréments l'indice de la prochaîne carte à distribuer
    self.indexNextCarte = (self.jeu[-1])
    return carte


  def distribuerJeu(self, nbJoueurs, nbCartes):
    ''' Cette méthode distribue nbCartes à chacun des nbJoueurs, si nbJoueurs X nbCartes <= self.tailleJeu.
    nbJoueurs: Nombre de joueurs devant recevoir nbCartes (type int)
    nbCartes: Nombre de cartes à distribuer à chaque joueur (type int)
    Valeur retournée: une liste des listes de cartes distribuées à chaque joueur (liste de nbJoueurs listes, chaque sous-liste étant une liste de nbCartes objets de type Carte)
    '''
    # On essaie de faire la distribution des cartes
    try:
      # S'il n'y a pas assez de cartes, on lance une exception "TropDeCartesDistribuees"
      if (nbJoueurs * nbCartes > nbCartes):
        return TropDeCartesDistribuees
      # Liste qui contiendra les listes des cartes distribuées à chaque joueurs
      tableau = []

      # On créé une liste de cartes vide pour chaque joueur
      for i in range(nbJoueurs):
        main = []
        tableau.append(main)

      # On va distribuer nbCartes à chaque joueurs
      for i in range(nbJoueurs):
        for j in range(nbCartes):
        # On distribue à tour de rôle une carte à chaque joueur, jusqu'à ce qu'ils aient tous nbCartes
        # On récupère la liste de cartes du i-ème joueur
            tableau[i].append(self.distribuerCarte())
            # On ajoute une carte à cette liste

      pass

    except TropDeCartesDistribuees as n:
      # Cette exception est captée lorsque le nombre de cartes à distribuer est supérieur au nombre total de cartes disponible dans le jeu
      # On affiche un message donnant le nombre de cartes que l'on demandait de distribuer
      print(TropDeCartesDistribuees.__doc__, n)
      raise


########################################################
#################### Test du module ####################
########################################################
if (__name__ == '__main__'):

  jeu52 = JeuCartes(52)
  jeu52.melanger()

  for carte in jeu52.getJeu():
    print('Nom:', carte.getNom())
    print('Couleur:', carte.getCouleur())
    print('Valeur:', carte.getValeur())
    print('Nom de fichier image:', carte.getNomImg())

  # Distribution de 5 cartes à 3 joueurs
  distribution_3_joueurs_5_cartes_par_joueur = jeu52.distribuerJeu(3, 5)
  for i in range(3):
    print('Joueur', i+1, ':')
    listeCartes = distribution_3_joueurs_5_cartes_par_joueur[i]
    for c in listeCartes:
      print(c.getNom(), 'de', c.getCouleur())

  # Distribution de 10 cartes à 6 joueurs pour générer une exception (6X10 > 52)
  distribution_6_joueurs_10_cartes_par_joueur = jeu52.distribuerJeu(6, 10)

  for i in range(6):
    # S'il y a une exception, distribution_6_joueurs_10_cartes_par_joueur a pour valeur None
    if not(distribution_6_joueurs_10_cartes_par_joueur is None):
      print('Joueur', i+1, ':')
      listeCartes = distribution_6_joueurs_10_cartes_par_joueur[i]
      for c in listeCartes:
        print(c.getNom(), 'de', c.getCouleur())