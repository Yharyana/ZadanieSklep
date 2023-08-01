from sklep.produkty import *
def lista(listar):
    input_b=0.0
    input_ilosc =0.0

    x=True
    listar = listar[""]
    while x==True and __name__=='__main__':
        j = 1
        inpute=input("hej chcesz dodać coś do listy zamowien? By zobaczyc prodkuty cene itp wcisnij A by dodac cos wcisnij B by zzakonnczyć program wscisnij X")
        if inpute=='X':
            x=False
        elif inpute=="A":
            for i in produktyr:

                print(f" to jest produkt numer   {j}  {i}")
                j+=1
            j = 1
            for i in ceny_per_kilo:

                print(f" to jest cena produktu numer   {j}  {i} zł")
                j+=1
            j = 1
            for i in dostepnosc_w_kilo:

                print(f" to jest dostepnosc prodkutku nr   {j}  {i} kg ")
                j+=1
        else:
            input_b=input("dobra to który chcesz produkt na swoja liste zakupów? ( napisz 1,2 badz 3")
            input_ilosc=("i jak duzo ma tego byc?")




