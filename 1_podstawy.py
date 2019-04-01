print("CDV")
print(2)

'''
no fajnie
'''

potega = 2 ** 10

print(potega)

# pobieranie danych z klawiatury
print("Podaj imie.")

imie = input()

#konkatenacja +
print("Twoje imie podane z klawiatury: " + imie)

print("Podaj nazwisko.")

nazwisko = input()

print("Twoje nazwisko podane z klawiatury to: " + nazwisko)
print()

# Twoje imie: ..., Twoje nazwisko: ..

print("Twoje imie: " + imie + ", twoje nazwisko: " + nazwisko)

'''
Użytkownik podaje z klawiatury swój wiek,
wyświetl dane w formacie: Twój wiek: ... lat
'''

print()
print("Podaj swój wiek: ", end="")
wiek = input()
print(type(wiek)) #str
print("Twój wiek:", wiek, "lata")

wiek1 = 20
print(type(wiek1)) #int
#print ("Twój wiek:" + wiek1 + "lata")
print("Twój wiek:", wiek1, "lata")

nazwisko = "Kowalski"
PierwszyZnak = nazwisko[0]
print(PierwszyZnak)

dlugosc = len(nazwisko)
print(dlugosc)

ostatniZnak = nazwisko[len(nazwisko) - 1]
print(ostatniZnak)

ostatniZnak = nazwisko[-1]
print(ostatniZnak)
