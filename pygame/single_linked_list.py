class SingleLinkedList:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    """ Por fuera de la clase nodo """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def show_list(self):
        # 1. Declarar una array vacío que contendraá los valores de los nodos de SLL
        array_with_nodes_value = list()
        current_node = self.head 
        # Mientras el nodo actual que estoy visitando sea diferente de None
        while(current_node != None):
            # Añado al final de la lista el valor extraido del nodo
            array_with_nodes_value.append(current_node.value)
            # Visito el próximo nodo antes de salir del while
            current_node = current_node.next
        # Imprimimos la lista
        print(array_with_nodes_value)
        return array_with_nodes_value
    
    def create_node_sll_ends(self, value):
        # Creamos una variable que va a tener la estructura de un nodo
        new_node = self.Node(value)
        # Validar si la SLL tiene nodos o no
        if self.head == None:
            # Al nuevo nodo se convierte en la cabeza y cola de la lista
            self.head = new_node
            self.tail = new_node
        else:
            # Si ingresa en esta condición, es porque ya existe al menos un nodo
            # 1. Debemos relacionar al nuevo nodo con la cola de la lista
            # 2. Convertir al nuevo nodo en la cola de la lista
            self.tail.next = new_node
            self.tail = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length +=1
    
    def create_node_sll_unshift(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            print(self.head.value)
        else:
            new_node.next = self.head
            self.head = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length +=1

    def delete_node_sll_pop(self):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            current_node = self.head
            new_tail = current_node
            while current_node.next != None:
                new_tail = current_node
                current_node = current_node.next
            print(f'Valor del nodo a eliminar es: {self.tail.value}')
            self.tail = new_tail
            self.tail.next = None
            self.length -= 1

    '''Eliminar nodo al inicio de la lista'''
    def shift_node_sll(self):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:

            self.head = None
            self.tail = None
            self.length -= 1
        else:
            remove_node = self.head
            print(f'Valor del nodo a eliminar es: {remove_node.value}')
            self.head = remove_node.next
            self.length -=1


    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while(index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node

    def get_node_value(self, index):
        if index < 1 or index > self.length:
            print('No se encontro')
        elif index == 1:
            return self.head.value
        elif index == self.length:
            return self.tail.value
        else:
            current_node = self.head
            node_counter = 1
            #Validar que el nodo a consultar sea el mismo del contador
            while(index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node.value

    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
            print(f'Actualizando el valor del nodo ...\n           >> {search_node.value} << a\n           >>{new_value}<<')
            search_node.value = new_value
        else:
            print("     >> No se encontro el nodo <<") 
            
    def remove_node(self, index):
        if index == 1:
            self.shift_node_sll()
        elif index == self.length:
            self.delete_node_sll_pop()
        else:
            remove_node_sll = self.get_node(index)
            if remove_node_sll!= None:
                previous_node = self.get_node(index - 1)
                print(self.get_node(index).value)
                previous_node.next = remove_node_sll.next
                remove_node_sll.next = None
                self.length-=1
            else:
                print('     >> No se encontro el nodo <<')
    

    def show_SLL_length(self):
        return self.length

    def search_an_element_and_return_index(self, value):
        if(self.length==0):
            print('La lista esta vacia')
        elif(self.head.value==value):
            return 1
        elif(self.tail.value==value):
            return self.length
        else:
            current_node=self.head
            counter=1
            while(current_node!=None):
                if(current_node.value==value):
                    return counter
                else:
                    current_node=current_node.next
                    counter+=1
                if(counter==self.length):
                    print('El elemento buscado no se encuentra')           

    def reverse(self):
        if self.length > 1:
            aux_head = self.tail
            aux_tail = self.head
            if self.length == 2:
                self.head = aux_head
                self.head.next = aux_tail
                self.tail = aux_tail
                self.tail.next = None
                return
            
            current_node = self.tail
            for i in range (1, self.length - 1):
                node = self.get_node(self.length - i)
                current_node.next = node
                current_node = node
            node.next = aux_tail
            self.head = aux_head
            self.tail = aux_tail
            self.tail.next = None
    
    def eliminate_all_elements(self):
        self.head=None
        self.tail=None
        self.length=0

    def sort_all_elements(self):
        array_with_nodes_value = []
        current_node = self.head 
        while(current_node != None):
            array_with_nodes_value.append(current_node.value)
            current_node = current_node.next

        array_with_nodes_value.sort()

        current_node_2=self.head
        cont=0
        while(current_node_2 != None):
            current_node_2.value=array_with_nodes_value[cont]
            cont+=1
            current_node_2 = current_node_2.next

    def add_node_in_index(self, index, value):
        max_length=12
        if self.length != max_length:
            print(f"\n >>>>>> Agregar nodo en la posición {index} <<<<<<")
            if index == 1:
                self.create_node_sll_unshift(value)
            elif index == self.length + 1:
                self.create_node_sll_ends(value)
            else:
                new_node = self.Node(value)
                actual_node_sll = self.get_node(index)
                if actual_node_sll != None:
                    previous_node = self.get_node(index - 1)
                    print("Se va a mover: ",actual_node_sll.value)
                    previous_node.next = new_node
                    new_node.next = actual_node_sll
                    self.length+=1
                else:
                    print(" >>> El índice no es accesible <<< ")
            return True
        return False
    
    def eliminate_duplicate(self,value):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        else:
            if self.validate_has_duplicate(value):
                for item in self.show_list():
                        if item == value:
                            self.eliminate_by_value(item)
                
    def validate_has_duplicate(self,value):
        cont=0
        for item in self.show_list():
            if item == value:
                cont+=1
        if cont >=2:
            return True
        else:
            return False

    def eliminate_by_value(self,value):
        if self.head == None:
            print("lista vacia")
        elif self.head.value == value:
            self.shift_node_sll()
        elif self.tail.value == value:
            self.delete_node_sll_pop()
        else:
            index=1
            current_node=self.head
            while current_node != None:
                if current_node.value == value:
                    previous_node = self.get_node(index- 1)
                    previous_node.next = current_node.next
                    current_node.next=None
                current_node=current_node.next
                index+=1
            self.length-=1
    def eliminate_all_duplicates(self):
        if self.head is None:
            return
        current_node=self.head
        values=set()
        while current_node is not None:
            if current_node.value in values:
                self.eliminate_by_value(current_node.value)
            values.add(current_node.value)
            current_node=current_node.next
        print(values)

    def unir_duplicados(self):
        if self.head is None:
            return
        index=1
        
        values=set()
        for item in self.show_list():
            if self.validate_has_duplicate(item):
                index2=1
                for item2 in self.show_list():
                    if item2 == item and item in values:
                        self.remove_node(index2)
                        self.add_node_in_index(index,item)
                    index2+=1 
            if item not in values:
                values.add(item)
            index+=1
                        




    def empty_list(self):
        if(self.length==0):
            print('La Lista esta vacia')
        else:
            print('La lista no esta vacia, tiene un tamaño de ', self.length)