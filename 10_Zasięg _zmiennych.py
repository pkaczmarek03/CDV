##Zasięg zmiennych, zmienne lokalne i globalne

#Precyzja liczby (zaokrąglenie do 3 liczb po przecinku)

x= "{0:.3f}".format(5)
print(x)

def plnToChf(value):
    kursChf = 3.7913
    iloscChf = value / kursChf
    iloscChf = "{0:.4f}".format(iloscChf)
    print(f"Ilosc Chf: {iloscChf}")
    
plnToChf(400)
    
    
# uwtwórz fukncje zwracajaca ilosc euro jakią klient chce kupic#


def plnToEuro(value):
    kursEuro = 4.2847
    iloscEuro = value / kursEuro
    iloscEuro = "{0:.4f}".format(iloscEuro)
    print(f"Ilosc Euro: {iloscEuro}")
    

pln = input()
euro = plnToEuro(float(pln))

##print(f"Ilosc: {pln}PLN = {euro}Euro")

    
    
    
    
    
    
    
    
    
    
    
    
    
