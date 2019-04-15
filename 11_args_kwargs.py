import os
##print("test")




def wyswietl(number1, number2):
    print(f"Liczba1: {number1}")
    print(f"Liczba2: {number2}")

wyswietl(2,3)



################## Args


def wyswietlArgs(number1, *args):
     print(f"\n Pierwszy element: {number1}")
     for i in args:
         print(f"nastepny: {i}")


wyswietlArgs(2, 11, 23, 34)

##os.system("cls")
