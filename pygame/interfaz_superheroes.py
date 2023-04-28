import pygame, sys, webbrowser
from single_linked_list import SingleLinkedList
from combo_box import ComboBox
class interfas:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1100,700))
        pygame.display.set_caption("pygame")
        #sll
        self.inst=SingleLinkedList()
        #colores
        self.negro = (0,0,0)
        self.blanco = (255,255,255)
        self.gris = (155,155,155)
        self.verde = (0,187,45)
        self.verdeoscuro = (0,207,46)
        self.azul = (0,26,255)
        self.rojoclaro = (226,65,65)
        #aca van las imagenes
        self.batman= pygame.image.load("batman.jpg")
        self.batman= pygame.transform.scale(self.batman,(225,225))
        self.fondo= pygame.image.load("dc_logoPro.jpg")
        self.fondo=pygame.transform.scale(self.fondo,(1100,700))
        self.superman = pygame.image.load("superman.jpg")
        self.superman= pygame.transform.scale(self.superman,(225,225))
        self.detectivemarciano= pygame.image.load("Detective.marciano.jpg")
        self.detectivemarciano= pygame.transform.scale(self.detectivemarciano,(225,225))
        self.flash= pygame.image.load("flash.jpg")
        self.flash = pygame.transform.scale(self.flash,(225,225))
        self.mujermaravilla = pygame.image.load("mujer_maravilla.jpg")
        self.mujermaravilla = pygame.transform.scale(self.mujermaravilla,(225,225))
        self.fondoventanaprincipal = pygame.image.load("ventanaprincipal.jpg")
        self.fondoventanaprincipal = pygame.transform.scale(self.fondoventanaprincipal,(1100,610))
        self.iconogithub= pygame.image.load("icono_github.png")
        self.iconogithub= pygame.transform.scale(self.iconogithub,(70,60))
        #cabezas
        self.batmancabeza = pygame.Rect(104,263,225,225)
        self.supermancabeza = pygame.Rect(395,263,225,225)
        self.detectivemarcianocabeza= pygame.Rect(693,253,225,225)
        #imagenes metodos cuadrados
        self.metodobatman= pygame.Rect(24,224,175,175)
        self.metodosuperman= pygame.Rect(238,224,175,175)
        self.metodomujermaravilla= pygame.Rect(463,224,175,175)
        self.metodoflash= pygame.Rect(891,224,175,175)
        self.metododetective= pygame.Rect(677,224,175,175)
        self.cuadradogithub = pygame.Rect(706,619,70,60)
        self.seleccionarmarcar = pygame.Rect(0,0,0,0)
        #booleanos
        self.boolbatman=False
        self.booldetective=False
        self.boolmujermaravilla=False
        self.boolsuperman=False
        self.boolflash=False
        self.boolgithub=False
        "cabezas"
        self.boolbatmancabeza=False
        self.boolsupermancabeza=False
        self.booldetectivecabeza=False
        "control ventanas"
        self.controlventanaSLL=False
        self.controlventanaprincipal=True
        self.metodossll=False
        "metodo"
        self.verificar=False
        self.imagenseleccionada=""
        #combobox
        self.combo_rect = pygame.Rect(310,130,306,51)
        self.combo = ComboBox(self.screen ,["agregar al inicio", "agregar al final", "eliminar el primero", "eliminar el ultimo", "invertir", "eliminar todos", "eliminar con indice", "insertar con indice", "actualizar con indice"], self.combo_rect, self.gris, "Arial", 22, 5, self.negro, self.negro, 40, "Seleccione una opción")
        self.combo2_rect= pygame.Rect(815,126,100,51)
        self.combo2 = ComboBox(self.screen ,["1"], self.combo2_rect, self.gris, "Arial", 22, 5, self.negro, self.negro, 40, "")
        #botones
        self.clickbotonSLL=False
        self.clickbotonDLL=False
        self.clickbotonPilasyColas=False
        self.clickArboles=False
        self.clickGrafos=False
        self.clickaceptarmetodos=False
        "boton para devolverse a la ventana principal"
        self.inicio=pygame.Rect(930,34,124,44)
        self.clickinicio=False

        


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if self.controlventanaprincipal:
                self.ventanaprincipal()

            if self.controlventanaSLL:
                self.ventanaicialSLL()
                
            if self.metodossll:
                self.cambiarametodossll()
                
            
            
            pygame.display.flip()

    def texto(self, text, color, dimensiones,x,y):
        fuente=pygame.font.SysFont("Impact",dimensiones)
        superficie= fuente.render(text,True,(color))
        self.screen.blit(superficie,(x,y))
    
    def imagen(self,x,y,img,tam):
        img= pygame.transform.scale(img,(tam,tam))
        self.screen.blit(img,(x,y))
        borde= pygame.draw.rect(self.screen,self.gris,(x,y,tam,tam),5,0)
        if borde.collidepoint(pygame.mouse.get_pos()):
            borde= pygame.draw.rect(self.screen,self.verde,(x,y,tam,tam),5,0)

    def escogercabeza(self):
        if self.clickbotones(self.batmancabeza,self.boolbatmancabeza):
            self.boolbatmancabeza=True
            self.controlventanaSLL=False
            self.metodossll=True
            self.inst.create_node_sll_unshift("batman")
        elif self.clickbotones(self.supermancabeza,self.boolsupermancabeza):
                self.boolsupermancabeza=True
                self.controlventanaSLL=False
                self.metodossll=True
                self.inst.create_node_sll_unshift("superman")
        elif self.clickbotones(self.detectivemarcianocabeza,self.booldetectivecabeza):
                self.booldetectivecabeza=True
                self.controlventanaSLL=False
                self.metodossll=True
                self.inst.create_node_sll_unshift("detective marciano")

    def cambiarametodossll(self):
        if self.boolbatmancabeza or self.booldetectivecabeza or self.boolsupermancabeza:
            self.controlventanaSLL=False
            self.screen.blit(self.fondo,(0,0))
            self.texto("Single Linked List", self.negro, 25,18,47)
            self.texto("seleccione un metodo",self.negro,25,24,140)
            self.texto("posicion",self.negro,25,670,140)
            self.texto("estado actual de la lista", self.negro, 25, 8,423)
            self.imagen(24,224,self.batman,175)
            self.imagen(238,224, self.superman,175)
            self.imagen(463,224, self.mujermaravilla,175)
            self.imagen(677,224,self.detectivemarciano,175)
            self.imagen(891,224, self.flash,175)
            pygame.draw.rect(self.screen,self.gris,(310,130,306,51))
            pygame.draw.rect(self.screen,self.gris,(815,126,100,51))
            botonmetodos=pygame.draw.rect(self.screen,self.negro,(950,126,100,51))
            self.boton("Aceptar",self.verde,botonmetodos,0, 16, 25,self.negro,950,126,100,51)
            self.showlist()
            self.boton("Inicio",self.verde,self.inicio,0, 16, 25,self.negro,930,34,124,44)
            if self.clickbotones(self.inicio,self.clickinicio):
                self.inst.eliminate_all_elements()
                self.volveralinicio()
            if self.clickbotones(botonmetodos,self.clickaceptarmetodos):
                self.seleccionarmarcar = (0,0,0,0)
                self.metodosSLLsinIndex()
                self.inst.show_list()
            self.retornarimagenpresionada()
            pygame.draw.rect(self.screen,self.verde,self.seleccionarmarcar,5,0)
            self.combo.draw()
            self.combo2.draw()
            


            
            
    def boton(self, text, button_color, background_rect, border, border_radius, text_size, text_color,x,y,w,h):
        boton=pygame.draw.rect(self.screen, button_color, background_rect, border, border_radius)
        font = pygame.font.SysFont("Arial", text_size,True)
        render_text = font.render(text, True, text_color, None)
        self.screen.blit(render_text, (background_rect.x + (background_rect.width - render_text.get_width())/2, background_rect.y + (background_rect.height - render_text.get_height())/2))
        if boton.collidepoint(pygame.mouse.get_pos()):
            boton= pygame.draw.rect(self.screen,self.verdeoscuro,(x,y,w,h),5,0)
    
    def showlist(self):
        for i in range(1,self.inst.length+1):
            if self.inst.get_node_value(i) == "batman":
                self.ponerimagenenposicion(i,self.batman)
            elif self.inst.get_node_value(i) == "superman":
                self.ponerimagenenposicion(i,self.superman)
            elif self.inst.get_node_value(i) == "detective marciano":
                self.ponerimagenenposicion(i,self.detectivemarciano)
            elif self.inst.get_node_value(i) == "mujer maravilla":
                self.ponerimagenenposicion(i,self.mujermaravilla)
            elif self.inst.get_node_value(i) == "flash":
                self.ponerimagenenposicion(i,self.flash)

    def ponerimagenenposicion(self,index,imagen):
        if index == 1:
            self.imagen(73,460,imagen,100)
        elif index == 2:
            self.imagen(235,460,imagen,100)
        elif index == 3:
            self.imagen(398,460,imagen,100)
        elif index == 4:
            self.imagen(561,460,imagen,100)
        elif index == 5:
            self.imagen(724,460,imagen,100)
        elif index == 6:
            self.imagen(886,460,imagen,100)
        elif index == 7:
            self.imagen(73,570,imagen,100)
        elif index == 8:
            self.imagen(235,570,imagen,100)
        elif index == 9:
            self.imagen(398,570,imagen,100)
        elif index == 10:
            self.imagen(561,570,imagen,100)
        elif index == 11:
            self.imagen(724,570,imagen,100)
        elif index == 12:
            self.imagen(886,570,imagen,100)
    
    def metodosSLLsinIndex(self):
        if self.combo.getIndex() == 0:
            if self.imagenseleccionada != "" and self.inst.length<12:
                self.inst.create_node_sll_unshift(self.imagenseleccionada)
        if self.combo.getIndex() == 1:
            if self.imagenseleccionada != "" and self.inst.length<12:
                self.inst.create_node_sll_ends(self.imagenseleccionada)
        if self.combo.getIndex() == 2:
            if self.inst.length<12:
                self.inst.shift_node_sll()
        if self.combo.getIndex() == 3:
            if self.inst.length<12:
                self.inst.delete_node_sll_pop()
        if self.combo.getIndex() == 4:
            if self.inst.length<12:
                self.inst.reverse()
        if self.combo.getIndex() == 5:
            if self.inst.length<12:
                self.inst.eliminate_all_elements()
        if self.combo.getIndex() == 6:
            if self.combo2.getIndex() != -1:
                self.inst.remove_node(self.combo2.getIndex()+1)
        if self.combo.getIndex() == 7:
            if self.combo2.getIndex() != -1 and self.imagenseleccionada !="":
                self.inst.add_node_in_index(self.combo2.getIndex()+1,self.imagenseleccionada)
        if self.combo.getIndex() == 8:
            if self.combo2.getIndex() != -1 and self.imagenseleccionada !="":
                self.inst.update_node_value(self.combo2.getIndex()+1, self.imagenseleccionada)
        self.imagenseleccionada=""
        data_list = [str(x) for x in range(1, self.inst.show_SLL_length() + 1)]
        self.combo2.updateOptions(data_list)

    
    def retornarimagenpresionada(self):
        if self.clickbotones(self.metodobatman, self.boolbatman):
            self.imagenseleccionada="batman"
            self.seleccionarmarcar = self.metodobatman
            return True
        elif self.clickbotones(self.metodosuperman, self.boolsuperman):
            self.seleccionarmarcar = self.metodosuperman
            self.imagenseleccionada="superman"
            return True
        elif self.clickbotones(self.metodoflash, self.boolflash):
            self.imagenseleccionada="flash"
            self.seleccionarmarcar = self.metodoflash
            return True
        elif self.clickbotones(self.metodomujermaravilla,self.boolmujermaravilla):
            self.seleccionarmarcar = self.metodomujermaravilla
            self.imagenseleccionada="mujer maravilla"
            return True
        elif self.clickbotones(self.metododetective,self.booldetective):
            self.seleccionarmarcar = self.metododetective
            self.imagenseleccionada="detective marciano"
            return True
        
    def ventanaprincipal(self):
        self.screen.fill(self.rojoclaro)
        self.screen.blit(self.fondoventanaprincipal,(0,0))
        botonSLL=pygame.draw.rect(self.screen,self.azul,(398,94,303,44))
        self.boton("Single Linked List",self.azul,botonSLL,0, 16, 25,self.blanco,398,94,303,44)
        botonDLL=pygame.draw.rect(self.screen,self.azul,(398,187,303,44))
        self.boton("Double Linked List",self.azul,botonDLL,0, 16, 25,self.blanco,398,187,303,44)
        botonPilasYColas=pygame.draw.rect(self.screen,self.azul,(398,280,303,44))
        self.boton("Pilas Y Colas",self.azul,botonPilasYColas,0, 16, 25,self.blanco,398,280,303,44)
        botonArboles=pygame.draw.rect(self.screen,self.azul,(398,373,303,44))
        self.boton("Arboles",self.azul,botonArboles,0, 16, 25,self.blanco,398,373,303,44)
        botonGrafos=pygame.draw.rect(self.screen,self.azul,(398,466,303,44))
        self.boton("Grafos",self.azul,botonGrafos,0, 16, 25,self.blanco,398,466,303,44)
        if self.clickbotones(botonSLL,self.clickbotonSLL):
            self.controlventanaprincipal=False
            self.controlventanaSLL=True
        self.texto("desarrolado por: santiago lesmes marin",self.negro,20,390,621)
        self.texto("@1 SEM - 2023",self.negro,20,500,651)
        self.screen.blit(self.iconogithub,(706,619))
        if self.clickbotones(self.cuadradogithub,self.boolgithub):
            webbrowser.open(r"https://github.com/slesmes/pygame.git")

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
        
    def ventanaicialSLL(self):
        self.screen.blit(self.fondo,(0,0))
        self.imagen(104,263,self.batman,225)
        self.imagen(395,263,self.superman,225)
        self.imagen(693,263,self.detectivemarciano,225)
        self.texto("SingleLinkedList",self.negro,40,10,44)
        self.texto("Seleccione la cabeza",self.negro,40,370,120)
        self.escogercabeza()
        self.boton("Inicio",self.verde,self.inicio,0, 16, 25,self.negro,930,34,124,44)
        if self.clickbotones(self.inicio,self.clickinicio):
            self.volveralinicio()

    def volveralinicio(self):
        self.controlventanaSLL=False
        self.controlventanaprincipal=True
        self.metodossll=False
        self.boolbatmancabeza=False
        self.booldetectivecabeza=False
        self.boolsupermancabeza=False

if __name__ == "__main__":
    a=interfas()
    a.run()
