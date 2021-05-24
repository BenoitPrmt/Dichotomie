# Dichotomie
Algorithmes dichotomiques.
Si jamais vous avez des améliorations à proposer pour modifier ces codes n'hésitez pas à faire une **pull request** !

**Codes réalisés pour m'entrainer en Python**

## Recherche Dichotomiques

**Le principe est le suivant :**
On recherche une valeur x dans une liste L triée (dans l'ordre croissant par exemple).
On vérifie l'élément y du milieu de liste :
```
- S'il a pour valeur x, c'est terminé (on retourne son rang).
- Si y < x, alors x est maintenant à chercher dans la partie de liste se trouvant à droite de l'élément y (c'est à dire dans les éléments d'indice plus grand que l'indice de y).
- Si y > x, alors x est maintenant à chercher dans la partie de liste se trouvant à gauche de l'élément y.
```

## Activité Indiana Jones

4 personnages veulent traverser un pont suspendu le plus rapidement
possible. Seulement, le pont est en très mauvais état et
il fait nuit, ce qui impose deux contraintes :

```
• le pont peut supporter maximum deux personnes à la fois (sinon il craque)
• il faut une lampe torche pour chaque traversée pour ne pas tomber, vu qu’il manque des planches sur le pont.
```

Malheureusement nos quatre personnes n’ont qu’**une seule torche à se partager**, et il faut donc qu’il y ait à chaque fois une personne qui ramène la torche. De plus, quand deux personnes traversent, le plus rapide doit attendre le plus lent sinon l’un des deux n’a plus de torche.

Les temps de traversée des personnages sont :

```
• 5 mn pour l’aventurière qui connaît le pont comme sa poche
• 10 mn pour Indiana Jones, en pleine forme mais qui découvre le pont
• 20 mn pour leur premier acolyte, blessé
• 25mn pour leur deuxième acolyte, plus gravement blessé.
```

De plus, un peuple cannibale est à la poursuite de la petite équipe et arrivera dans 61 minutes.

## Activité d'organisation de planning

On cherche à optimiser l’utilisation d’une salle de sport. On considère un ensemble d’activités, chacune possédant une date de début et une date de fin. Pour des raisons logistiques, on ne peut pas programmer des activités se déroulant en même temps.

**La question est la suivante :** Quel est le nombre maximal d’activités que l’on va pouvoir planifier afin d'optiminser un maximum la salle de sport ?

Considérons un ensemble d'activités avec pour chaque activité un début et une fin :
```
S=((‘A’,1,4),(‘B’,0,6),(‘C’,3,5),(‘D’,12,13),(‘E’,8,11),(‘F’,8,12),(‘G’,2,13),(‘H’,6,10),(‘I’,5,9),(‘J’,3,8),(‘K’,5,7),(‘L’13,16),(‘M’,15,17),(‘N’,16,19))
```

## Tri à bulles

Le tri à bulle consiste à parcourir le tableau, par exemple de gauche à droite, en comparant les éléments côte à côte et en les permutant s'ils ne sont pas dans le bon ordre. Au cours d'une passe du tableau, les plus grands éléments remontent de proche en proche vers la droite comme des bulles vers la surface.
On s'arrête dès que l'on détecte que le tableau est trié : si aucune permutation n'a été faite au cours d'une passe.
