import rozne as mis
import time

depozyt = -1
while depozyt <= 0:
    depozyt = float(input("Podaj swoj depozyt: "))

while depozyt > 0:

    print("Twoje obecne fundusze: " + str(depozyt))
    zaklad = 0
    while zaklad <= 0 or zaklad > depozyt:
        zaklad = float(input("Podaj zaklad: "))
    Przegrana = False

    karty_gracza = []
    karty_krupiera = []
    gracz_punkty = 0
    krupier_punkty = 0
    licznik_asow = 0
    klicznik_asow = 0

    karta1 = "[" + mis.draw_card() + "]"
    if karta1 == "[A]":
        licznik_asow += 1
    karty_gracza.append(karta1)
    gracz_punkty += int(mis.points(karta1))

    karta2 = "[" + mis.draw_card() + "]"
    if karta2 == "[A]":
        licznik_asow += 1
    karty_gracza.append(karta2)
    gracz_punkty += int(mis.points(karta2))

    if karta1 == "[A]" and gracz_punkty > 21:
        gracz_punkty = gracz_punkty - 10
        licznik_asow = licznik_asow - 1
    elif karta2 == "[A]" and gracz_punkty > 21:
        gracz_punkty = gracz_punkty - 10
        licznik_asow = licznik_asow - 1

    Kkarta1 = "[" + mis.draw_card() + "]"
    if Kkarta1 == "[A]":
        klicznik_asow += 1
    karty_krupiera.append(Kkarta1)
    krupier_punkty += int(mis.points(Kkarta1))

    Kkarta2 = "[" + mis.draw_card() + "]"
    if Kkarta2 == "[A]":
        klicznik_asow += 1
    karty_krupiera.append(Kkarta2)

    krupier_blackjack = False
    gracz_blackjack = False
    if Kkarta1 == "[A]":
        if Kkarta2 == "[K]" or Kkarta2 == "[Q]" or Kkarta2 == "[J]" or Kkarta2 == "[10]":
            krupier_blackjack = True
    elif Kkarta2 == "[A]":
        if Kkarta1 == "[K]" or Kkarta1 == "[Q]" or Kkarta1 == "[J]" or Kkarta1 == "[10]":
            krupier_blackjack = True

    if karta1 == "[A]":
        if karta2 == "[K]" or karta2 == "[Q]" or karta2 == "[J]" or karta2 == "[10]":
            gracz_blackjack = True
    elif karta2 == "[A]":
        if karta1 == "[K]" or karta1 == "[Q]" or karta1 == "[J]" or karta1 == "[10]":
            gracz_blackjack = True

    koniec = False
    while not koniec:

        if krupier_blackjack:
            krupier_punkty = 21
        if gracz_blackjack:
            gracz_punkty = 21

        if krupier_blackjack == True and gracz_blackjack == False:
            mis.pokaz_karty(karty_krupiera, krupier_punkty, karty_gracza, gracz_punkty)
            print("Krupier ma Blackjacka - Przegrales :(")
            print()
            depozyt = depozyt - zaklad
            Koniec = True
            break

        elif krupier_blackjack == False and gracz_blackjack == True:
            krupier_punkty = mis.points(karty_krupiera[0]) + mis.points(karty_krupiera[1])
            mis.pokaz_karty(karty_krupiera, krupier_punkty, karty_gracza, gracz_punkty)

            if Kkarta1 == "[A]" and krupier_punkty > 21:
                krupier_punkty = krupier_punkty - 10
                klicznik_asow = klicznik_asow - 1
            elif Kkarta2 == "[A]" and krupier_punkty > 21:
                krupier_punkty = krupier_punkty - 10
                klicznik_asow = klicznik_asow - 1

            print("Masz Blackjacka - Wygrales 150% zakladu :))")
            print()
            depozyt = depozyt + 1.5 * zaklad
            Koniec = True
            break

        elif krupier_blackjack and gracz_blackjack:
            mis.pokaz_karty(karty_krupiera, krupier_punkty, karty_gracza, gracz_punkty)
            print("Podwojny blackjack - Remis, Zaklad wraca do ciebie")
            print()
            Koniec = True
            break

        print()
        print("Karty Krupiera: ")
        time.sleep(0.5)
        print(Kkarta1 + "[ ]")
        print("Krupier ma " + str(krupier_punkty) + " punktow")
        print()
        print("Karty Gracza: ")
        for karta in karty_gracza:
            print(karta + " ", end="")
            time.sleep(0.5)
        print("Masz " + str(gracz_punkty) + " punktow")
        print()

        print("1. Dobierz")
        print("2. Spasuj")

        wybor = 0
        while wybor < 1 or wybor > 2:
            wybor = int(input("Wybierz: "))

        if wybor == 1:
            x = "[" + mis.draw_card() + "]"
            karty_gracza.append(x)

            if x == "[A]":
                licznik_asow += 1

            gracz_punkty += int(mis.points(karty_gracza[-1]))
            if gracz_punkty > 21 and licznik_asow > 0:
                gracz_punkty = gracz_punkty - 10
                licznik_asow = licznik_asow - 1

            if gracz_punkty > 21:
                print()
                print("Koniec gry")
                krupier_punkty = mis.points(karty_krupiera[0]) + mis.points(karty_krupiera[1])

                if Kkarta1 == "[A]" and krupier_punkty > 21:
                    krupier_punkty = krupier_punkty - 10
                    klicznik_asow = klicznik_asow - 1
                elif Kkarta2 == "[A]" and krupier_punkty > 21:
                    krupier_punkty = krupier_punkty - 10
                    klicznik_asow = klicznik_asow - 1

                mis.pokaz_karty(karty_krupiera, krupier_punkty, karty_gracza, gracz_punkty)

                print("Przegrales :(")
                print()
                depozyt = depozyt - zaklad
                koniec = True
                break

        elif wybor == 2:
            krupier_punkty = mis.points(karty_krupiera[0]) + mis.points(karty_krupiera[1])

            if Kkarta1 == "[A]" and Kkarta2 == "[A]":
                klicznik_asow = 1
                krupier_punkty = krupier_punkty - 10

            if krupier_punkty > 16:
                mis.pokaz_karty(karty_krupiera, krupier_punkty, karty_gracza, gracz_punkty)

            while krupier_punkty <= 16:
                if len(karty_krupiera) == 2:
                    mis.pokaz_karty(karty_krupiera, krupier_punkty, karty_gracza, gracz_punkty)
                    time.sleep(1.5)

                print("Krupier dobiera...")
                print()
                time.sleep(1)

                y = "[" + mis.draw_card() + "]"

                if y == "[A]":
                    klicznik_asow += 1

                karty_krupiera.append(y)
                krupier_punkty += int(mis.points(karty_krupiera[-1]))

                if krupier_punkty > 21 and klicznik_asow > 0:
                    krupier_punkty = krupier_punkty - 10
                    klicznik_asow = klicznik_asow - 1

                mis.pokaz_karty(karty_krupiera, krupier_punkty, karty_gracza, gracz_punkty)
                time.sleep(1.5)

            if krupier_punkty > 21:
                print("Wygrales :)")
                print()
                depozyt = depozyt + zaklad
                Koniec = True
                break
            elif 21 >= krupier_punkty > gracz_punkty:
                print("Przegrales :(")
                print()
                depozyt = depozyt - zaklad
                Koniec = True
                break
            elif krupier_punkty <= 21 and krupier_punkty < gracz_punkty:
                print("Wygrales :)")
                print()
                depozyt = depozyt + zaklad
                Koniec = True
                break
            elif krupier_punkty == gracz_punkty:
                print("Remis, Zaklad wraca do ciebie")
                print()
                koniec = True
                break

    if depozyt <= 0:
        print("Niewystarczajace srodki!")
        print()
