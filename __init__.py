import sys
import pygame
from pygame.locals import*
pygame.init()
import class5Mas

#dimenciones de ventana
altura=800
ancho=600

def main():
    pygame.init()
    #Variables de la clase
    img_dado=class5Mas.dados
    puntos=class5Mas.Puntos
    suma_puntos=class5Mas.Sumar
    ver_ganador=class5Mas.VerfGanador
    #creacion de ventana
    screen=pygame.display.set_mode((altura,ancho))
    pygame.display.set_caption("5 mas")
    #Jugadores
    j1=0
    j2=0
    #letrero turnos
    tj1="El jugador #1 ha lanzado"
    tj2="El jugador #2 ha lanzado"
    #letrero ganador
    gana_j1="El ganador es el jugador #1"
    gana_j2="El ganador es el jugador #2"
    #imagen de teclas
    teclas=pygame.image.load("img/teclas.png").convert()
    #imagen fondo
    fondo=pygame.image.load("img/fondo.png").convert()
    #cargar dados
    d1=pygame.image.load("img/1.png").convert()
    d2=pygame.image.load("img/6.png").convert()
    #TURNO
    turno=1
    tirada=0
    puntos_tirada=0
    #bucle principal
    while True:
        screen.blit(fondo,(0,0))
        screen.blit(d1,(350,150))
        screen.blit(d2,(350,250))
        screen.blit(teclas,(500,200))
        for evento in pygame.event.get():
            if evento.type==QUIT:
                sys.exit(0)
            elif evento.type==KEYUP:
                if evento.key==K_SPACE:
                    dado1=class5Mas.LanzarDado()
                    dado2=class5Mas.LanzarDado()
                    d1=pygame.image.load(img_dado(dado1)).convert()
                    d2=pygame.image.load(img_dado(dado2)).convert()
                    screen.blit(d1,(350,150))
                    screen.blit(d2,(350,250))
                    #print dado1
                    #print dado2
                if turno%2==0 and tirada>=3:
                    letra30=pygame.font.SysFont("Arial",20)
                    imagenTextoPresent=letra30.render(tj2,True,(50,50,50),(0,0,0))
                    rectanguloTextoPresent=imagenTextoPresent.get_rect()
                    rectanguloTextoPresent.centerx=150
                    rectanguloTextoPresent.centery=250
                    screen.blit(imagenTextoPresent,rectanguloTextoPresent)
                    p=puntos(dado1,dado2,j1,puntos_tirada)
                    #print p
                    if p[0]=="puntos":
                        j2=p[1]
                    else:
                        j2=j2+p[1]
                    tirada=tirada+1
                    if tirada==6:
                        tirada=0
                        turno=turno+1
                    if ver_ganador(j2)==True:
                        l30=pygame.font.SysFont("Arial",30)
                        iTP=l30.render(gana_j2,True,(50,50,50),(0,0,0))
                        rTP=iTP.get_rect()
                        rTP.centerx=150
                        rTP.centery=300
                        screen.blit(iTP,rTP)
                    #sumatoria de puntos
                else:
                    letra30=pygame.font.SysFont("Arial",20)
                    imagenTextoPresent=letra30.render(tj1,True,(50,50,50),(0,0,0))
                    rectanguloTextoPresent=imagenTextoPresent.get_rect()
                    rectanguloTextoPresent.centerx=150
                    rectanguloTextoPresent.centery=250
                    screen.blit(imagenTextoPresent,rectanguloTextoPresent)
                    p=puntos(dado1,dado2,j1,puntos_tirada)
                    #print p
                    if p[0]=="puntos":
                        j1=p[1]
                    else:
                        j1=j1+p[1]
                    tirada=tirada+1
                    if tirada==3:
                        turno=turno+1
                    if ver_ganador(j1)==True:
                        l30=pygame.font.SysFont("Arial",30)
                        iTP=l30.render(gana_j1,True,(50,50,50),(0,0,0))
                        rTP=iTP.get_rect()
                        rTP.centerx=150
                        rTP.centery=300
                        screen.blit(iTP,rTP)

            #IMPREION DE MARCADORES
            puntos_j1=str(j1)
            letra=pygame.font.SysFont("Arial",30)
            img_j1=letra.render(puntos_j1,True,(50,50,50),(0,0,0))
            r_j1=img_j1.get_rect()
            r_j1.centerx=50
            r_j1.centery=50
            screen.blit(img_j1,r_j1)

            puntos_j2=str(j2)
            letra=pygame.font.SysFont("Arial",30)
            img_j1=letra.render(puntos_j2,True,(50,50,50),(0,0,0))
            r_j1=img_j1.get_rect()
            r_j1.centerx=500
            r_j1.centery=50
            screen.blit(img_j1,r_j1)

            pygame.display.flip()

if __name__=="__main__":
    main()
