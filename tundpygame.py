import pygame
import sys
import math

pygame.init()
ekraan = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Esimene aken")

kollane = (255, 255, 0)
roheline = (0, 255, 0)
sinine = (0, 0, 255)
hall = (100, 100, 100)
lilla = (150, 0, 150)
roosa = (255, 100, 255)
valge = (255, 255, 255)
must = (0, 0, 0)
tume_roheline = (0, 100, 0)

def joonista_paike(ekraan, x, y):
    for i in range(0, 360, 10):
        dx = math.cos(math.radians(i)) * 100
        dy = math.sin(math.radians(i)) * 100
        pygame.draw.line(ekraan, kollane, (x, y), (x + dx, y + dy), 2)
    pygame.draw.circle(ekraan, kollane, (x, y), 40)

def joonista_lill(ekraan, x, y):
    for r in range(60, 10, -10):
        pygame.draw.circle(ekraan, roosa, (x, y), r)
    pygame.draw.rect(ekraan, tume_roheline, (x - 10, y, 20, 150))

def joonista_pilv(ekraan, x, y):
    pygame.draw.circle(ekraan, hall, (x, y), 40)
    pygame.draw.circle(ekraan, hall, (x + 40, y), 50)
    pygame.draw.circle(ekraan, hall, (x + 80, y + 10), 40)

def joonista_mesilane(ekraan, x, y):
    mesilane = pygame.image.load("mesilanee2.xcf")
    mesilane = pygame.transform.scale(mesilane, (80, 80))
    ekraan.blit(mesilane, (x, y))

ekraan.fill(sinine)
pygame.draw.rect(ekraan, roheline, (0, 300, 800, 300))

joonista_paike(ekraan, 0, 0)
joonista_lill(ekraan, 400, 300)
joonista_pilv(ekraan, 600, 100)
joonista_mesilane(ekraan, 360, 180)

font = pygame.font.SysFont("comicsansms", 48)
tekst = font.render("Tere tulemast!", True, valge)
ekraan.blit(tekst, (230, 50))
pygame.display.flip()

while True:
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

