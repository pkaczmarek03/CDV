def witaj():
    print("witaj", end=" ")
    print("Janusz")

witaj()

def wyswietlWiek(wiek):
    print("Masz", wiek, "lata")

wyswietlWiek(23)

##def iloczyn(a, b):
 ##   return a * b
##print(iloczyn(3,4))


##def iloraz (a,b):
##    return a / b
##print(iloraz(4,3))
##print(iloraz(b=10, a=2))

###############################

#Przekazywanie argrumentów przez referencje

def show(name):
    print(f"Przed modyfikacją: {name}")
    name[0] = "Beata"
    name[1] = "Barbara"
    name[2] = "Bogdan"
    print(f"Po modyfikacji: {name}")
    print(f"ID Po modyfikacji: {id(name)}")


data = ["Anna", "Agnieszka", "Andrzej"]
print(f"Przed wywolaniem funkcji show: {data}")
print(f"ID Po modyfikacji: {id(data)}")
show(data)
print(f"Po wywolaniem funkcji show: {data}")




###### Słownik

data1 = {0: "Artur", 1: "Andrzej"}
print(f"\n ID przed modyfikacją: {id(data1)}")
show(data1)


###### Przekazanie argumentu przez wartość


def show1(city):
    print(f"Przed modyfikacją: {city}")
    city[0] = "Berlin"
    city[1] = "Londyn"
    print(f"Po modyfikacji: {city}")
    print(f"ID Po modyfikacji: {id(city)}")


miasto = ["Gniezno", "Poznań"]

print(f"Przed wywołaniem fukcji show1: {miasto}")
print(f"ID obietku miasto: {id(miasto)}")
show1(list(miasto))
print(f"Po wywołaniu fukcji show1: {miasto}")




