from math import lgamma
import random
#-----initialisation-----#
class loup_garou:
    def __init__(self) -> None:
        self.role=["loup","voyante","vollageois"]
        self.pseudo={}
        self.name
        self.nb_joueur=len(self.name)
        self.mort= []

    def nb_player(self):
        return self.nb_joueur

    def distrib_role(self):
        distrib = {}
        while (self.role != 0 or self.nb_joueur != 0):
            a = random.randrange(self.nb_joueur)
            b = random.randrange(self.role)
            player ={self.nb_joueur[a]:self.role[b]}
            distrib.append(player)
            self.nb_joueur.remove(self.nb_joueur[a])
            self.role.remove(self.role[b])
        return distrib
    

    def nom_role(self):
        return self.role
#-----jour-----#
def tuer(self):
        phrase = ''
        for i in self.mort:
            del(self.name[i])
            phrase += ', ' + i

        if len(self.mort)>1:
            return 'Les joueurs ' + phrase + ' sont morts cette nuit'
        elif len(self.__tue) == 1:
            return 'Le joueur ' + str(self.mort[0]) + ' est mort cette nuit'
        else :
            return "Personne n'est mort cette nuit"

def assign_capitaine(self,pseudo):
        maxi = []
        vote = {pseudo:vote}
        for i in vote.keys():
            if vote[i] >= max(vote.values()) :
                maxi.append(i)
            if len(maxi)>1:
                a = random.randint(0,len(maxi)-1)
                joueur = maxi[a]

        self.capitaine = joueur

def design_capitaine(self):
        capitaine = input("Le défunt capitaine nomme son succésseur : ")
        self.__capitaine = capitaine


#-----nuit-----#
def voyante(self,distrib):
        self.nom()
        nom=input("la voyante se réveille et donne le nom de la personne qu'elle veux connaître : ")
        print("Cette personne est : ",distrib[nom])

def loup(self):
        self.nom()
        print("les loups se réveillent")
        votes = input('Entrez le dictionnaire des votes (loup) : ')
        self.vote(votes)
