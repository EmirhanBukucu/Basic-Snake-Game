import pygame
import sys
import random

#Ayarlar
genislik = 600
yukseklik = 400

#Renkler
SIYAH = (0, 0, 0)
KOYU_GRI = (20, 20, 20)
BLOK_BOYUTU = 20

#Mekanikler
FPS = 10
BASLANGIC_HIZI = 10
PUAN_ARALIGI = 5

#Oyun Penceresi Ayarları
pygame.init()
ekran = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("Ramazan GameCode Camp Basic Snake Game")
saat = pygame.time.Clock()

#Mekanik Ayarlamaları
yilan = [(genislik // 2, yukseklik // 2)]
yon = (0, 0)
yem = (random.randint(0, (genislik - BLOK_BOYUTU) // BLOK_BOYUTU ) * BLOK_BOYUTU,
       random.randint(0, (yukseklik - BLOK_BOYUTU) // BLOK_BOYUTU ) * BLOK_BOYUTU)

skor = 0
seviye = 1
skor_font = pygame.font.Font(None, 36)

#Oyun Döngüsü
calisiyor = True
while calisiyor:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisiyor = False

        #Girdiler
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP and yon != (0, 1):
                yon = (0, -1)
            elif event.key == pygame.K_DOWN and yon != (0, -1):
                yon = (0, 1)
            elif event.key == pygame.K_LEFT and yon != (1, 0):
                yon = (-1, 0)
            elif event.key == pygame.K_RIGHT and yon != (-1, 0):
                yon = (1, 0)

    #Yılan'ın Uzaması İçin Gereken Sistem
    yeni_bas = (yilan[0][0] + yon[0] * BLOK_BOYUTU, yilan[0][1] + yon[1] * BLOK_BOYUTU)
    if yeni_bas[0] < 0 or yeni_bas[0] >= genislik or yeni_bas[1] < 0 or yeni_bas[1] < 0 or yeni_bas[1] >= yukseklik or  yeni_bas in yilan[1:]:
        calisiyor = False
    else:
        yilan.insert(0, yeni_bas)
        if yeni_bas == yem:
            skor += 1
            if skor % PUAN_ARALIGI == 0:
                seviye += 1
                FPS += 1
            yem = (random.randint(0, (genislik - BLOK_BOYUTU) // BLOK_BOYUTU) * BLOK_BOYUTU,
                 random.randint(0, (yukseklik - BLOK_BOYUTU) // BLOK_BOYUTU) * BLOK_BOYUTU)
        else:
            yilan.pop()
    ekran.fill(SIYAH)

    #UI Ayarlamaları
    for x in range(0, genislik, BLOK_BOYUTU):
        for y in range(0, yukseklik, BLOK_BOYUTU):
            if (x + y) // BLOK_BOYUTU % 2 == 0:
                pygame.draw.rect(ekran, KOYU_GRI, (x, y, BLOK_BOYUTU, BLOK_BOYUTU))
            else:
                pygame.draw.rect(ekran, SIYAH, (x, y, BLOK_BOYUTU, BLOK_BOYUTU))
    skor_yazi = skor_font.render("Skor: {}".format(skor), True, (255, 255, 255))
    seviye_yazi = skor_font.render("Seviye: {}".format(seviye), True, (255, 255, 255))
    ekran.blit(skor_yazi, (10, 10))
    ekran.blit(seviye_yazi, (genislik-150, 10))

    for parca in yilan:
        pygame.draw.rect(ekran, (0, 255, 0), (parca[0], parca[1], BLOK_BOYUTU, BLOK_BOYUTU))
    
    pygame.draw.rect(ekran, (255, 0, 0), (yem[0], yem[1], BLOK_BOYUTU, BLOK_BOYUTU))

    pygame.display.flip()
    saat.tick(FPS)

#Oyun Sonu
pygame.quit()
sys.exit()