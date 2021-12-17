# Python et les Objects ![coucou](https://www.avisto.com/wp-content/uploads/2017/10/developpeur-python.jpg)

https://www.youtube.com/watch?v=h6jciR8K43E
https://www.youtube.com/watch?v=Y-wXK0Wu5pc&t=710s

# https://replit.com/@bisbis/pythonyoutube2h#main.py

# Pour penser Orienté Object il faut :

## L'object Parent Type qui comprend ( ==L'entité== -> ==ce qui va definir la # classe== ) :

## ---- Le constructeur , def--init-- , ==qui contient les self==

## ----Les objets de la personne ( ==Son nom , Sa taille, Son age== )

## ---- Les actions de la personne ( ==Ce qu'elle fait ou ce qu'elle va faire== ) --> ==Se sont les # méthodes==

Exemple pour creer un object , on l'appelle de cette maniere :

```sh
class Voiture:
        marque="lamborghini"
        couleur="rouge"

```

si maintenant je veux copier cet OBJECT je peux faire :

```sh
Voiture_Copier = Voiture():
par contre si je fais
print(Voiture_Copier.marque)
-> il me sortira lamborghini

```

Creation d'un objet parent
def **init** permet de definir le parent selon le modele qui suit ( ici make , model,year)
a completer avec self.make en dessous

```sh
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

Enfant1 = Car('Chevy', 'sonic', 2015)

print(Enfant1.get_descriptive_name())
```

### ==au dessus on peut voir Enfant1 qui appelle lobjet parent et choisi ses propres charactéristiques==

## autre exemple :

```self
class Personne:
  def __init__(self,nom,age,color):
    self.nom = nom
    self.age = age
    self.color = color
    print("salut ")


  def sepresenter(self):


    print("je mappelle " + self.nom + " j'ai " + self.age +" ans , ma couleur préférée est " + self.color)

  def autrefonction():
    print("ceci est une methode de classe")



```

personne2 = Personne("boris","30","bleu") -> personne2 devant un enfant de personne avec ses caracteristiques
personne2.sepresenter() -> on appelle la fonction sepresenter avec ses propres carac, grace au self
==sortie -> je mappelle boris j'ai 30 ans , ma couleur préférée est bleu==

Personne.autrefonction() -> ici pas de self , on appelle la fonction qu'on a mis dans l'object .

```

# On peut alterer le nom de l object enfant ->

personne2.nom = 'igor'

personne2.sepresenter()

OUTPUT : je mappelle ==igor== j'ai 30 ans , ma couleur préférée est bleu


```

On peut appeller une fonction de la classe parent dans une autre , exemple ::::

```

class Personne:
  def __init__(self,nom,age,color):
    self.nom = nom
    self.age = age
    self.color = color
    print("salut ")


  def sepresenter(self):

    print("je mappelle " + self.nom + " j'ai " + self.age +" ans , ma couleur préférée est " + self.color)
    if self.Estmajeur()
        print("je suis majeur")
    --->>>>> la fonction Estmajeur est appellée avec le self Estmajeur .

  def Estmajeur():
    return self.age>=18


```
