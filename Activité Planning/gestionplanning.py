# Fonction qui test si une activité est compatible avec celles déjà prises.
def compatible(test,listeActivite):
    b=True
    for ele in listeActivite:
        #Test si une des bornes de l'activité est comprise entre les bornes d'une activité précédente.
        if ele[1]<test[1]<ele[2] or ele[1]<test[2]<ele[2]:
            b=False
            break
         #Test si une les bornes de l'activité englobent une autre activité précédente.
        if ele[1]>=test[1] and ele[2]<=test[2]:
            b=False
            break
    return b
# Déclaration des activités
tabActivite=[(1,4,'A'),(0,6,'B'),(3,5,'C'),(12,13,'D'),(11,8,'E'),(8,12,'F'),(2,13,'G'),(6,10,'H'),(5,9,'I'),(3,8,'J'),(5,7,'K'),(13,16,'L'),(15,17,'M'),(16,19,'N')] 
tabActiviteAvecDuree=[]
# Création de la liste des activités avec leur durée.
for ele in tabActivite:
    duree=ele[1]-ele[0]
    tup=(duree,ele[0],ele[1],ele[2])
    tabActiviteAvecDuree.append(tup)

# Tri de la liste des activités par durée.
tabDureeTrie= sorted(tabActiviteAvecDuree)
# Création de la liste des activités avec la première activité.

listeActivite=[]
listeActivite.append(tabDureeTrie[0])


tabDureeTrie.pop(0) #On enlève la première activité déjà prise de la liste.


# On détermine si pour chaque acitivté celle-ci est compatible ou non et si on l'ajoute.
for ele in tabDureeTrie:
    b=compatible(ele,listeActivite)
    if b:
        listeActivite.append(ele)

# On créer la liste finale en ne prenant que le nom de l'activité.
listeFinale=[]
for ele in listeActivite:
    listeFinale.append(ele[3])
print("La liste des activités sera :",listeFinale)
