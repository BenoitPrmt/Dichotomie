dico={"aventurière":5,"indiana":10,"doctor":20,"acolyte":25}

min=dico.get("doctor")
print(min)
tempsTot=0

for nom,temps in dico.items():
    if temps<min:
        min=temps
        rapide=nom

print(min)
print(rapide)

for nom,temps in dico.items():
    if nom==rapide:
        pass
    else:
        tempsTot=tempsTot+temps+min
        
print('Le temps total est de {} minutes'.format(tempsTot))