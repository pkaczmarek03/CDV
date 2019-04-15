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

print(f"Ilosc: {pln}PLN = {euro}Euro")


#Zmienna Globalna#

kursUSD = 3.7899
print(f"ID USD: {id(kursUSD)}")

def plnToUSD(value):
    ##kursUSD = 3.7899
    iloscUSD = value / kursUSD
    iloscUSD = "{0:.4f}".format(iloscUSD)
    ##print(f"Ilosc USD: {iloscUSD}")
    return iloscUSD

print(f"Kurs USD: {kursUSD}")
pln = input()
usd = plnToUSD(float(pln))
print(f"Ilosc: {pln}PLN = {usd}USD")
    
    
zmiennaGlobalna = 10
print(f"\n Wartosc zmiennaGlobalna: {zmiennaGlobalna}")
print(f"ID zmiennaGlobalna: {id(zmiennaGlobalna)}")
      
def spr():
      global zmiannaGlobalna
      zmiennaGlobalna = 20
      print(f"\n Wartosc zmiennaGlobalna: {zmiennaGlobalna}")
      print(f"\n ID zmiennaGlobalna: {id(zmiennaGlobalna)"})
    
spr()
            
print(f"\n Wartosc zmiennaGlobalna po wywolaniu fukncji: {zmiennaGlobalna}")
print(f"\n ID zmiennaGlobalna po wywolaniu funkcji: {id(zmiennaGlobalna)}")
    
    
    
    
    
    
    
