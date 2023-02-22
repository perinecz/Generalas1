import random

#0
print("Egy emberi név generálása.")

vNevek=["Ádám", "Balogh", "Lakatos", "Tóth", "Rézműves", "Váradi"]
ferfiKNevek=["András", "Béla", "Géza", "József", "István"]
noiKNevek=["Anita","Ildikó","Erika","Mariann"]

#1
neme=input("Kérem az ember nemét (férfi/nő): ")

if neme.lower()=="férfi":
    teljesNev = random.choice(vNevek)+' '+random.choice(ferfiKNevek)
elif neme.lower()=="nő":
    teljesNev = random.choice(vNevek)+' '+random.choice(noiKNevek)
else:
    print("HIBA: rossz nemet adott meg")
    exit()

#2-3
print(teljesNev)
