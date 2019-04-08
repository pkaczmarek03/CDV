slownik = {"klucz": "wartosc1", "klucz2":"wartosc2"}

pracownik = {"imie:":"Janusz", "nazwisko:":"Tracz", "wiek:":23, "miasto:":"Poznań", "imionaDzieci:":["Grażyna", "Henryk"], "imionaRodzicow:": ["Jacek", "Wacek"]}
print(pracownik)

klucz = "wiek"
if klucz in pracownik:
    del pracownik[klucz]
    print(f"klucz {klucz} zostal usuniety")
else:
    print("klucz nie zostal usuniety")

print(pracownik.keys())
print(pracownik.values())
print(list(pracownik.values()))
print(pracownik.items())

for value in pracownik.values():
    print(value, sep=" ")


for key, value in pracownik.items():
    print(key, value)
