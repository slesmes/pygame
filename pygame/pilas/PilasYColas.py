import pygame, sys, webbrowser
class Pilas:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1100,700))
        #colores
        self.negro = (0,0,0)
        self.blanco = (255,255,255)
        self.gris = (155,155,155)
        self.verde = (0,187,45)
        self.verdeoscuro = (0,207,46)
        self.azul = (0,26,255)
        self.rojoclaro = (226,65,65)
        self.cafe = (101,30,30)
        #imagenes
        self.fondo= pygame.image.load("pilas/fondoblackjack.jpg")
        self.fondo= pygame.transform.scale(self.fondo,(1100,700))
        self.crupier= pygame.image.load("pilas/crupier.png")
        self.crupier=pygame.transform.scale(self.crupier,(230,300))
        #booleanos
        self.verificar=False
        self.clickinicio=False
        


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.principal()
            inicio=pygame.draw.rect(self.screen,self.cafe,(930,30,128,38))
            self.boton("inicio",self.cafe,inicio,0, 16, 25,self.negro,930,30,128,38)
            pygame.display.flip()
            if self.clickbotones(inicio,self.clickinicio):
                return True
            else:
                return False
            



    def principal(self):
        self.screen.blit(self.fondo,(0,0))        
        pedircartas=pygame.draw.rect(self.screen,self.cafe,(500,217,180,36))
        self.boton("pedir carta",self.cafe,pedircartas,0, 16, 25,self.negro,500,217,180,36)
        self.imagen(400,35,self.crupier,230,300)
        self.texto("jugador 1",self.blanco,20,100,357)
        jugador1=pygame.draw.rect(self.screen,self.cafe,(207,350,137,36))
        self.boton("plantarme",self.cafe,jugador1,0, 16, 25,self.negro,207,350,137,36)
        self.texto("jugador 2",self.blanco,20,425,523)
        jugador2=pygame.draw.rect(self.screen,self.cafe,(551,523,137,36))
        self.boton("plantarme",self.cafe,jugador2,0, 16, 25,self.negro,551,523,137,36)
        self.texto("jugador 3",self.blanco,20,780,349)
        jugador3=pygame.draw.rect(self.screen,self.cafe,(887,349,137,36))
        self.boton("plantarme",self.cafe,jugador3,0, 16, 25,self.negro,887,349,137,36)
        self.texto("presione start para comenzar",self.blanco,20,15,32)
        start=pygame.draw.rect(self.screen,self.cafe,(312,30,128,38))
        self.boton("start",self.cafe,start,0, 16, 25,self.negro,312,30,128,38)
        

    def inicio(self):
        if self.clickinicio:
                return True
        else:
            return False
        
        
    def clickbotones(self,cuadradoboton,clickboton):
        if cuadradoboton.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not clickboton and self.verificar:
                clickboton=True
                self.verificar = False
                return True
        if not pygame.mouse.get_pressed()[0]:
            clickboton=False
            self.verificar = True
            return False
            
    def imagen(self,x,y,img,alto,ancho):
        img= pygame.transform.scale(img,(ancho,alto))
        self.screen.blit(img,(x,y))


    def boton(self, text, button_color, background_rect, border, border_radius, text_size, text_color,x,y,w,h):
        boton=pygame.draw.rect(self.screen, button_color, background_rect, border, border_radius)
        font = pygame.font.SysFont("Arial", text_size,True)
        render_text = font.render(text, True, text_color, None)
        self.screen.blit(render_text, (background_rect.x + (background_rect.width - render_text.get_width())/2, background_rect.y + (background_rect.height - render_text.get_height())/2))
        if boton.collidepoint(pygame.mouse.get_pos()):
            boton= pygame.draw.rect(self.screen,self.verdeoscuro,(x,y,w,h),5,0)

    def texto(self, text, color, dimensiones,x,y):
        fuente=pygame.font.SysFont("Impact",dimensiones)
        superficie= fuente.render(text,True,(color))
        self.screen.blit(superficie,(x,y))

    def clickbotones(self,cuadradoboton,clickboton):
        if cuadradoboton.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not clickboton and self.verificar:
                clickboton=True
                self.verificar = False
                return True
        if not pygame.mouse.get_pressed()[0]:
            clickboton=False
            self.verificar = True
            return False