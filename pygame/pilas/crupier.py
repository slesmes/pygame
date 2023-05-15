import random
class crupier:
    def __init__(self):
        self.score=0
        self.baraja=[]
        self.cartas=[]

    def barajar(self):
        while len(self.baraja) < 52:
            numeros = list(range(1, 14))
            random.shuffle(numeros)
            for i in numeros:
                if self.baraja.count(i) < 4:
                    self.baraja.append(str(i))

    def actualizar_score(self):
        self.score=sum([self.valor_carta(carta) for carta in self.cartas])
        num_ases=self.cartas.count("1")
        if self.score < 9 and num_ases:
            self.score += 10
            num_ases -= 1

    def actualizar_cartas(self):
        for i in range(len(self.cartas)):
            if self.cartas[i] == "1":
                self.cartas[i] = "as"
            elif self.cartas[i] == "11":
                self.cartas[i] ="j"
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
