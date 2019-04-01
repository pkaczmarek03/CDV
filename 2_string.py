tekst = ("Anna, paweł, JuliA")

lista = tekst.split(", ")
print(tekst)
print(lista)
print(type(lista)) #TypListy

imiel = lista[0]
print(imiel) #Anna

imieDuze = imiel.upper()
print(imieDuze)

imieMale = imiel.lower()
print(imieMale)

#sprawdzanie zawartości
print("\n Podaj swoje nazwisko:", end=" ")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc) #true or false

nazwisko = ""
print(nazwisko.isalpha()) #false

text1 = "Julia"
text2 = "Nowak"
print(text1 + text2)

text1 = text1.rstrip()
print(text1 + text2)
print(text1 + " " + text2)

#wyświetlenie łańcucha znaków

#wszystkie wersje Pythona
text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowsze wersje Pythona . 2.6
text = "{1}, Java i {0}".format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisanie danych

rok = 2019
miesiac = "kwiecień"
dzień = 1

print("\nData: ", end="")
print(dzień, miesiac, rok)


