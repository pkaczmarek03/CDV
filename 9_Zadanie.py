def dane():
    print("Podaj marke: ")
    marka = input()
    print("Podaj model: ")
    model = input()
    print("Podaj pojemnosc: ")
    pojemnosc = input()
    print("Podaj Max predkosc: ")
    maxPredkosc = input()

    samochod = {"marka:": marka, "model:": model, "pojemnosc:": pojemnosc, "MaxPojemnosc:": maxPredkosc}


    def czytanie(dane):
        print(dane(samochod))

dane()
czytanie()
