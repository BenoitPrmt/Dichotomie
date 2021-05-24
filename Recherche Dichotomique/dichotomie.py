L = [1, 2, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 70, 85]

nombre = int(input("Quel est le nombre recherché ?"))

tr = False
debut = 0
fin = len(L)

while not(tr) and debut<=fin:
    mil = (debut+fin)//2
    n = L[mil]
    print('Nouvel indice :', mil)
    print('Nouveau nombre :',n)
    if n==nombre:
        tr = True
    elif n<nombre:
        debut = mil + 1
    elif n>nombre:
        fin = mil - 1
        
if(tr):
    print("Le nombre est dans la liste !")
else:
    print("Le nombre n'est pas dans la liste !")
