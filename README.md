# Python et les Objects ![coucou](https://www.avisto.com/wp-content/uploads/2017/10/developpeur-python.jpg)

https://www.youtube.com/watch?v=h6jciR8K43E
https://www.youtube.com/watch?v=Y-wXK0Wu5pc&t=710s

### Pour penser Orienté Object il faut :

La personne Type ( ==L'entité== -> ==ce qui va definir la # classe== ) :
----Les objets de la personne ( ==Son nom , Sa taille, Son age== )
---- Les actions de la personne ( ==Ce qu'elle fait ou ce qu'elle va faire== ) --> ==Se sont les # méthodes==

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

Nomdunouvelobjetenfant = Car('Chevy', 'sonic', 2015)

print(my_new_car.get_descriptive_name())
```

### ==au dessus on peut voir nomdunouvelobject qui appelle lobjet parent et choisi ses propres charactéristiques== # debutpython
