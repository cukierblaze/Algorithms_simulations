import pygame
import random
import time

pygame.init()

szerokosc, wysokosc = 900, 700
okno = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("Snake")

bialy = (255, 250, 250)
czerwony = (255, 0, 0)
zielony = (173 ,255, 47)
czarny = (0, 0, 0)

rozmiar_bloku = 25
predkosc_weza = 15

czcionka = pygame.font.SysFont(None, 35)


def twoj_wynik(wynik):
    wartosc = czcionka.render("Twój wynik: " + str(wynik), True, bialy)
    okno.blit(wartosc, [0, 0])


def petla_gry():
    koniec_gry = False
    koniec_gry_info = False
    waz_x = szerokosc / 2
    waz_y = wysokosc / 2
    waz_x_zmiana = 0
    waz_y_zmiana = 0
    waz_lista = []
    dlugosc_weza = 1
    jedzenie_x = round(random.randrange(0, szerokosc - rozmiar_bloku) / rozmiar_bloku) * rozmiar_bloku
    jedzenie_y = round(random.randrange(0, wysokosc - rozmiar_bloku) / rozmiar_bloku) * rozmiar_bloku

    while not koniec_gry_info:
        while koniec_gry:
            okno.fill(czarny)
            twoj_wynik(dlugosc_weza - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        koniec_gry_info = True
                        koniec_gry = False
                    if event.key == pygame.K_c:
                        petla_gry()
                elif event.type == pygame.QUIT:
                    koniec_gry_info = True
                    koniec_gry = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                koniec_gry_info = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    koniec_gry_info = True
                if event.key == pygame.K_LEFT:
                    waz_x_zmiana = -rozmiar_bloku
                    waz_y_zmiana = 0
                elif event.key == pygame.K_RIGHT:
                    waz_x_zmiana = rozmiar_bloku
                    waz_y_zmiana = 0
                elif event.key == pygame.K_UP:
                    waz_y_zmiana = -rozmiar_bloku
                    waz_x_zmiana = 0
                elif event.key == pygame.K_DOWN:
                    waz_y_zmiana = rozmiar_bloku
                    waz_x_zmiana = 0

        waz_x += waz_x_zmiana
        waz_y += waz_y_zmiana

        if waz_x >= szerokosc or waz_x < 0 or waz_y >= wysokosc or waz_y < 0:
            koniec_gry = True

        glowa_weza = [waz_x, waz_y]
        waz_lista.append(glowa_weza)

        if len(waz_lista) > dlugosc_weza:
            del waz_lista[0]

        for segment in waz_lista[:-1]:
            if segment == glowa_weza:
                koniec_gry = True

        okno.fill(czarny)
        pygame.draw.rect(okno, czerwony, [jedzenie_x, jedzenie_y, rozmiar_bloku, rozmiar_bloku])
        rysuj_weza(rozmiar_bloku, waz_lista)

        pygame.display.update()

        if waz_x == jedzenie_x and waz_y == jedzenie_y:
            jedzenie_x = round(random.randrange(0, szerokosc - rozmiar_bloku) / rozmiar_bloku) * rozmiar_bloku
            jedzenie_y = round(random.randrange(0, wysokosc - rozmiar_bloku) / rozmiar_bloku) * rozmiar_bloku
            dlugosc_weza += 1

        pygame.time.Clock().tick(predkosc_weza)

    pygame.quit()
    quit()


def rysuj_weza(rozmiar_bloku, waz_lista):
    for x in waz_lista:
        pygame.draw.rect(okno, zielony, [x[0], x[1], rozmiar_bloku, rozmiar_bloku])


petla_gry()
