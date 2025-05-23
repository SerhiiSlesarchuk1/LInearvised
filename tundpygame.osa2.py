import pygame
import sys
pygame.init()

# Värvid
punane=[255, 0, 0]
taeva_sinine = [135, 206, 235]  
roheline=[0, 255, 0]
sinine=[0, 0, 255]
pink=[255, 153, 153]
hele_roheline=[153, 255, 153]  
pruun=[139, 69, 19]
hele_punane=[255, 200, 200]
tume_pruun=[101, 67, 33]
valge=[255, 255, 255]

# Ekraani seaded
ekraan=pygame.display.set_mode([640, 480])
pygame.display.set_caption("Maja")
ekraan.fill(taeva_sinine)  

# Maja joonistamise funktsioon
def joonista_maja(x, y, laius, korgus, pinnale, seina_varv, katuse_varv):
    
    seina_korgus=(3/4.0) * korgus
    pygame.draw.rect(pinnale, seina_varv, (x, y - seina_korgus, laius, seina_korgus))
    
    
    katuse_punktid=[(x, y - seina_korgus),(x + laius/2, y - korgus),(x + laius, y - seina_korgus)]
    pygame.draw.polygon(pinnale, katuse_varv, katuse_punktid)
    
   
    kontuuri_punktid=[(x, y - seina_korgus),(x, y),(x + laius, y),(x + laius, y - seina_korgus),(x, y - seina_korgus),(x + laius/2.0, y - korgus),(x + laius, y - seina_korgus)]
    joone_paksus=3
    pygame.draw.lines(pinnale, (0, 0, 0), False, kontuuri_punktid, joone_paksus)
    
    
    ukse_laius=laius*0.15
    ukse_korgus=korgus*0.25
    pygame.draw.rect(pinnale, pruun, (x + laius/2 - ukse_laius/2, y - ukse_korgus, ukse_laius, ukse_korgus))
    
    
    pygame.draw.circle(pinnale, (100, 100, 100),(int(x + laius/2 + ukse_laius/3), int(y - ukse_korgus/2)), 3)
    
    
    akna_suurus=laius * 0.12
    
    pygame.draw.rect(pinnale, valge, (x + laius*0.2, y - korgus*0.5, akna_suurus, akna_suurus))
    pygame.draw.rect(pinnale, sinine, (x + laius*0.2, y - korgus*0.5, akna_suurus, akna_suurus), 2)
    
    pygame.draw.line(pinnale, sinine, (x + laius*0.2, y - korgus*0.5 + akna_suurus/2),(x + laius*0.2 + akna_suurus, y - korgus*0.5 + akna_suurus/2), 2)
    pygame.draw.line(pinnale, sinine, (x + laius*0.2 + akna_suurus/2, y - korgus*0.5),(x + laius*0.2 + akna_suurus/2, y - korgus*0.5 + akna_suurus), 2)
    
    
    pygame.draw.rect(pinnale, valge, (x + laius*0.7, y - korgus*0.5, akna_suurus, akna_suurus))
    pygame.draw.rect(pinnale, sinine, (x + laius*0.7, y - korgus*0.5, akna_suurus, akna_suurus), 2)
    pygame.draw.line(pinnale, sinine, (x + laius*0.7, y - korgus*0.5 + akna_suurus/2),(x + laius*0.7 + akna_suurus, y - korgus*0.5 + akna_suurus/2), 2)
    pygame.draw.line(pinnale, sinine, (x + laius*0.7 + akna_suurus/2, y - korgus*0.5),(x + laius*0.7 + akna_suurus/2, y - korgus*0.5 + akna_suurus), 2)

maa_korgus=100
maa_y=480 - maa_korgus
pygame.draw.rect(ekraan, (34, 139, 34), (0, maa_y, 640, maa_korgus))

joonista_maja(100, maa_y, 300, 400, ekraan, hele_punane, tume_pruun)

pygame.draw.circle(ekraan, (255, 255, 0), (550, 80), 50)

pygame.display.flip()

while True:
    sündmus=pygame.event.poll()
    if sündmus.type==pygame.QUIT:
        break

pygame.quit()


