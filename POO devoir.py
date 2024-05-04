def Menu():
    print("menu")

def __Disponible__(self, Disponible):
   self.Disponible = Disponible
   print(Disponible)

def __Indisponible__(self, Indisponible):
    self.Indisponible = Indisponible
    print(Indisponible)

def __MenuBibliotheque__(self, MenuBibliotheque):
    self.MenuBibliotheque = MenuBibliotheque
    print("C'est le menu de l'application des bibliothéquaire")

def __MenuMembre__(self, MenuMembre):
    self.MenuMembre = MenuMembre
    print("C'est le menu de l'application des membres")
class Livre:
    name = "Le Livre De La Jungle"
    auteur = "Rudyard Kipling"
    dateEmprunt = "Aujourd'hui"
    disponible = ""
    def __init__(self, name):
        self.name = name


#Création des différents livres

Livre_01 = Livre
Livre_02 = Livre
Livre_03 = Livre
Livre_04 = Livre

#Informations dans les différentes class

Livre_01.name = "Harry Potter"
Livre_01.auteur = "De J. K. Rowling"
Livre_01.disponible = "est Disponible"

Livre_02.name = "StarWars"
Livre_02.auteur = "De George Lucas"
Livre_02.disponible = "est Disponible"

Livre_03.name = "Astérix le Gaulois"
Livre_03.auteur = "De René Goscinny"
Livre_03.disponible = "est Disponible"

Livre_04.name = "Boule et bill"
Livre_04.auteur = "De Jean Roba"
Livre_04.disponible = "est Disponible"



class Dvd:
    name = ""
    realisateur = ""
    dateEmprunt = "Aujourd'hui"
    disponible = ""
    def __init__(self, name):
        self.name = name

Dvd_01 = Dvd
Dvd_02 = Dvd
Dvd_03 = Dvd
Dvd_04 = Dvd


Dvd_01.name = "Harry Potter"
Dvd_01.auteur = "De J. K. Rowling"
Dvd_01.disponible = "est Disponible"


Dvd_02.name = "Star Wars"
Dvd_02.auteur = "De George Lucas"
Dvd_02.disponible = "est indisponible"


Dvd_03.name = "La Soupe Aux Choux"
Dvd_03.auteur = "De Louis de Funes"
Dvd_03.disponible = "est Disponible"


Dvd_04.name = "SpiderMan"
Dvd_04.auteur = "De Stan Lee"
Dvd_04.disponible = "est Disponible"


class Cd:
    name = ""
    artiste = ""
    dateEmprunt = "Aujourd'hui"
    disponible = ""


Cd_01 = Cd
Cd_02 = Cd
Cd_03 = Cd
Cd_04 = Cd


Cd_01.name = "Ipséité"
Cd_01.artiste = "De Damso"
Cd_01.disponible = "est Disponible"


Cd_02.name = "Or Noir"
Cd_02.artiste = "De Kaaris"
Cd_02.disponible = "est indisponible"


Cd_03.name = "A7"
Cd_03.artiste = "De SCH"
Cd_03.disponible = "est Disponible"


Cd_04.name = "Cicatrices"
Cd_04.artiste = "De Zola"
Cd_04.disponible = "est Disponible"

class JeuDePlateau :
    name = ""
    createur = ""
    disponible = "Indisponible à l'emprunt"

JeuDePlateau_01 = JeuDePlateau
JeuDePlateau_02 = JeuDePlateau
JeuDePlateau_03 = JeuDePlateau
JeuDePlateau_04 = JeuDePlateau


JeuDePlateau_01.name = "Monopoly"
JeuDePlateau_01.auteur = "De Elizabeth Magie"

JeuDePlateau_02.name = "La Bonne Paye"
JeuDePlateau_02.name = "De Paul J. Gruen"

JeuDePlateau_03.name = "Uno"
JeuDePlateau_03.auteur = "Merle Robbins"




