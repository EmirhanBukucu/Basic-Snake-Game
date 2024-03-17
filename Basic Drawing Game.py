import pygame
import sys

ekran_genislik = 800
ekran_yukseklik = 600

beyaz = (255, 255, 255)
siyah = (0,0,0)
yesil = (0, 255, 0)
kirmizi= (255,0,0)
mavi = (0,0, 255)

class CizimOyunu:
    def __init__(self):
        pygame.init()
        self.ekran = pygame.display.set_mode((ekran_genislik, ekran_yukseklik))
        pygame.display.set_caption("Ramazan GameCode Camp Basic Drawing Game")
        self.clock = pygame.time.Clock()
        self.cizim = False
        self.cizgi_rengi = siyah
        self.cizgi_kalinligi = 5
        self.cizim_yolu = []
    def run(self):
        running = True
        while running == True:
            self.clock.tick(60)
            self.ekran.fill(beyaz)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.cizim = True
                    self.cizim_yolu.append([])
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.cizim = False
                elif event.type == pygame.MOUSEMOTION and self.cizim == True:
                    pos = pygame.mouse.get_pos()
                    self.cizim_yolu[-1].append(pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.cizim_yolu = []
                    elif event.key == pygame.K_r:
                        self.cizgi_rengi = kirmizi
                    elif event.key == pygame.K_b:
                        self.cizgi_rengi = mavi
                    elif event.key == pygame.K_g:
                        self.cizgi_rengi = yesil
                    elif event.key == pygame.K_d:
                        self.cizgi_rengi = siyah
            self.cizim_ciz()
            pygame.display.flip()
        pygame.quit()
        sys.exit()
    def cizim_ciz(self):
        for yol in self.cizim_yolu:
            if len(yol) > 1:
                pygame.draw.lines(self.ekran, self.cizgi_rengi, False, yol, self.cizgi_kalinligi)
    
if __name__ == "__main__":
    oyun = CizimOyunu()
    oyun.run()