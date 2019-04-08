programowanie =["Python", "C#", "JS", "PHP", "Java"]

print(programowanie)
print(type(programowanie))

pierwszy = programowanie[0]
print(pierwszy)

trzyElementy = programowanie[0:3]
print(trzyElementy)

ostatni = programowanie[-1]
print(ostatni)

#Dodanie nowego elementu na koncu listy

programowanie.append("R")
programowanie.append("Python")
print(programowanie)

#Zlicznie elementów listy

ile = programowanie.count("Python")
print(ile)

#Ilosc elem w liscie

iloscElem = len(programowanie)
print(iloscElem)

#Polaczenie list

inneJezyki = ["C","C++"]
print("Polaczenie list")
programowanie.extend(inneJezyki)
print(programowanie)

#czyszczenie list

nowa = programowanie

print("Lista nowa: ", end="")
print(nowa)






