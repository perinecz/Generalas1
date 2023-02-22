import random

#0
print("Egy osztály tanulóinak generálása.")

vNevek=["Ádám", "Balogh", "Lakatos", "Tóth", "Rézműves", "Váradi"]
ferfiKNevek=["András", "Béla", "Géza", "József", "István"]
noiKNevek=["Anita","Ildikó","Erika","Mariann"]

db=int(input("Kérem a tanulók számát: "))
tanulok = []
for i in range(db):
    #tanulo neve
    neme=random.randint(1,2)
    if neme==1:
        teljesNev = random.choice(vNevek)+' '+random.choice(ferfiKNevek)
        neme="férfi"
    else:
        teljesNev = random.choice(vNevek)+' '+random.choice(noiKNevek)
        neme="nő"
    #tanulo születési ideje
    ev=random.randint(2000, 2005)
    honap=random.randint(1, 12)
    nap=random.randint(1, 28)

    datum = f"{ev}.{honap:0>2d}.{nap:0>2d}"
    #magasság
    magassag=random.randint(155, 190)

    #tanulo összeállítása
    tanulo = (teljesNev, datum, neme, magassag)

    #felvétel a tanulókhoz
    tanulok.append(tanulo)


#2-3
for item in tanulok:
    print(item)
