import pygame
pygame.init()
class playerx:
    def __init__(self,x,y,textox,textoy):
        self.score=0
        self.cartas=[]
        self.x=x
        self.y=y
        self.turno=False
        self.textox=textox
        self.textoy=textoy

    def actualizar_score(self):
        self.score=sum([self.valor_carta(carta) for carta in self.cartas])
        num_ases=self.cartas.count("1")
        if self.score < 11 and num_ases:
            self.score += 10
            num_ases -= 1

    def actualizar_cartas(self):
        for i in range(len(self.cartas)):
            if self.cartas[i] == "1":
                self.cartas[i] = "as"
            elif self.cartas[i] == "11":
                self.cartas[i] = "j"
            elif self.cartas[i] == "12":
                self.cartas[i] = "q"
            elif self.cartas[i] == "13":
                self.cartas[i] = "k"

    def valor_carta(self,carta):
        if carta == "as":
            return 1
        elif carta == "j" or carta == "q" or carta == "k":
            return 10
        else:
            return int(carta)
    
    def validaciones_pedir_carta(self):
        if self.score > 21:
            pierdes="Has perdido"
            self.turno=False
            return pierdes
        elif self.score == 21:
            gano="¡Blackjack! ganas"
            return gano
