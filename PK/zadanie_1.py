import unittest

def Ne(n,M0):
    x = n * M0 / 5252
    return x
def ihp (p, l, a, n, N):
    x = ((p * l * a * N * n) / 2) / 4500
    return x

def get_menu_choice():
    def print_menu():
        print(30 * "-", "Kalkulator mocy silnika", 30 * "-")
        print("1. oblicz moc podajac obroty silnika i moment obrotowy")
        print("2. oblicz indukowaną moc silnika I.H.P")
        print("3. wyjdz ze skryptu ")
        print(73 * "-")

    loop = True

    while loop:         # While loop bedzie dzialac do momentu loop = False
        print_menu()    # pokaz menu
        choice = input("wybierz [1-4]: ")

        if choice == '1':
            n = input ("podaj obroty silnika [obr/min]: ")
            M0 = input ("podaj moment obrotowy silnika [Nm]: ")
            moc = Ne(int(n), int(M0))
            print("Moc silnika [KM] =" ,moc)
            print("Moc silnika [kW] =" ,moc * 1.34)
            loop = False
        elif choice == '2':
            p = input("podaj ciśnienie [kg/cm2]: ")
            l = input("podaj dlugość suwu tłoka [cm]: ")
            a = input("podaj powierzchnie tłoka [cm2]: ")
            n = input("podaj obroty silnika [obr/min]: ")
            N = input("podaj ilość cylidrów: ")
            moc = ihp(int(p),int(l),int(a),int(n),int(N))
            print("Moc silnika I.H.P [KM] =", moc)
            loop = False
        elif choice == '3':
            int_choice = -1
            print("na dziś koniec..")
            loop = False  # to konczy petle

        else:
            # wybor inny niz 1-2 spowoduje blad
            input("Zły wybór, spróbuj ponownie..")

get_menu_choice()

class Ne_Case(unittest.TestCase):

    def test_Ne(self):
        result = Ne(3000, 422)
        assert result == 5

    def notatest(self):
        pass