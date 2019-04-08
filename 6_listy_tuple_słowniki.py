#Listy

imiona =["Julia", "Anna", "Tomasz"]
print(type(imiona))
imiona.append("Paweł")
print(len(imiona))


#Tuple

nazwiska = ("Nowak", "Kowalski")
print(nazwiska)
print(type(nazwiska))
print(len(nazwiska))

#Słowniki

osoba = {"imie": "Julia", "nazwisko":"Nowak", "wiek":25}
print(osoba)
print(type(osoba))

print(osoba["nazwisko"])
print(osoba.get("wzrost", "brak danych"))
print(osoba.get("imie", "brak danych"))
print(osoba.keys())
