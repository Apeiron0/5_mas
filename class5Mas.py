J1 = [0]
J2 = [0]
J3 = [0]
J4 = [0]

#class CincoMas:
def dados(dado):
    import pygame
    from pygame.locals import*
    pygame.init()

    if dado==1:
        d1="img/1.png"
    elif dado==2:
        d1="img/2.png"
    elif dado==3:
        d1="img/3.png"
    elif dado==4:
        d1="img/4.png"
    elif dado==5:
        d1="img/5.png"
    elif dado==6:
        d1="img/6.png"
    return d1


def NuevaPartida():
	J1[0] = 0
	J2[0] = 0
	J3[0] = 0
	J4[0] = 0

def Jugadores(Numero):
	if Numero == 0:
		return J1
	else:
		if Numero == 1:
			return J2
		else:
			if Numero == 2:
				return J3
			else:
				if Numero == 3:
					return J4

def LanzarDado():
	import random
	C = random.randrange(1,7)
	return C

#suma los puntos del turno de las tres lanzadas
#puntos son puntos totales

def Puntos(Dado1,Dado2,Puntos,Suma):
	if Dado1 == Dado2:
		if Dado1 == 3:
			Puntos = 0
			return ["puntos",Puntos]
		else:
			if Dado1 == 5:
				Suma = Suma + 20
				return ["suma",Suma]
			else:
				Suma = Suma + 15
				return ["suma",Suma]
	else:
		if Dado1 == 3 and Dado2 != 5 or Dado1 != 5 and Dado2 == 3:
			return ["puntos",Puntos]
		else:
			if Dado1 == 5 or Dado2 == 5:
				Suma = Suma + 5
				return ["suma",Suma]
			else:
				return ["suma",Suma]

def Sumar(Puntos,Suma):
	Puntos = Puntos + Suma
	return Puntos

def VerfGanador(Puntos):
	if Puntos>= 150:
		return True
	else:
		return False