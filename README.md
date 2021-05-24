# Dichotomie
Algorithmes dichotomiques

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
