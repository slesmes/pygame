import time
from memory_profiler import memory_usage
class Node:
    def __init__(self, data):
        self.data= data
        self.next = None
        self.prev = None

class Double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def add_node_at_end(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head= new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
        self.length+=1

    def add_node_at_start(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head= new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
    
    def add_node_at_index(self,data,index):
        new_node= Node(data)
        if index < 1 or index>self.length+1:
            raise IndexError("posicion fuera del rango")
        elif index==1:
            self.add_node_at_start(data)
        elif index == self.length+1:
            self.add_node_at_end(data)
        else:
            current_node = self.head
            for i in range(1, index-1):
                current_node = current_node.next
            new_node.next=current_node.next
            new_node.prev=current_node
            current_node.next.prev=new_node
            current_node.next=new_node
            self.length+=1     
            
    def print_list(self):
        if self.head is None:
            return print("lista vacia")
        current_node= self.head
        while current_node is not None:
            print(current_node.data, end=" | ")
            current_node= current_node.next

    def remove_at_start(self):
        if self.head is None:
            return
        else:
            self.head=self.head.next
            if self.head is not None:
                self.head.prev= None
            self.length-=1

    def remove_at_end(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head=None
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.prev.next=None
        self.length-=1
    
    def remove_node_at_index(self,position):
        if position < 1 or position > self.length:
            raise IndexError("Posición fuera de rango")
        current_node = self.head
        if position == 1:
            self.remove_node_at_start()
        elif position == self.length:
            self.remove_node_at_end()
        else:
            for i in range(1, position):
                current_node = current_node.next
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            self.length -= 1

    def remove_node_by_value(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.remove_at_start()
        current_node= self.head
        while current_node is not None:
            if current_node.data==value:
                if current_node.next is not None:
                    current_node.next.prev= current_node.prev
                current_node.prev.next= current_node.next
                return
            current_node=current_node.next
            self.length-=1

    def get_node_at_index(self, position):
        if position < 1 or position > self.length:
            raise IndexError("Posición fuera de rango")
        if self.head is None:
            return None
        current_node = self.head
        i = 1
        while current_node is not None and i < position:
            current_node = current_node.next
            i+=1
        return print(current_node.data)
    
    def update_node_at_value(self, old_data, new_data):
        if self.head is None:
            return
        current_node = self.head
        while current_node is not None:
            if current_node.data==old_data:
                current_node.data = new_data
                print("valor cambiado")
                return print(current_node.data)
            current_node = current_node.next

    def update_node_at_index(self, position, value):
        if position < 1 or position > self.length:
            raise IndexError('Posicion fuera de rango')
        if self.head is None:
            return
        current= self.head
        i=1
        while current is not None and i < position:
            current=current.next
            i+=1
        if current is not None:
            current.data = value
    
    def sort_asc(self):
        if self.head is None:
            return
        current_node=self.head
        while current_node.next is not None:
            next_node=current_node.next
            while next_node is not None:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data= next_node.data, current_node.data
                next_node=next_node.next
            current_node= current_node.next

    def has_duplicates(self):
        if self.head is None:
            return
        current_node=self.head
        values=set()
        while current_node is not None:
            if current_node.data in values:
                return print("hay duplicados")
            values.add(current_node.data)
            current_node=current_node.next
        print(values)
        return print("no duplicates")
    
    def has_dupicaltes_with_information(self):
        if self.head is None:
            return
        current_node= self.head
        values={}
        found_duplicates = False
        while current_node is not None:
            if current_node.data in values:
                values[current_node.data].append(current_node)
                found_duplicates=True
            else:
                values[current_node.data]=[current_node]
            current_node=current_node.next
        
        if found_duplicates:
            message= "los valores duplicados son "
            for value, nodes in values.items():
                if len(nodes)>1:
                    message+=f"{value}: {len(nodes)} veces \n"
                    #  message += ",".join([str(Node) for node in Nodes]) + "\n"
            print(message)
            return True
        else:
            return False
        
    def calculate_complexity(self, func):
        
        # Ejecutar la función una vez para que se compile
        func(0)

        # Calcular tiempo de ejecución
        start_time = time.time()
        func(0)
        end_time = time.time()
        exec_time = end_time - start_time

        # Calcular uso de memoria
        mem_usage = max(memory_usage((func, (0,)), interval=0.1))

        # Imprimir resultados
        print(f"Función {func.name}:")
        print(f"Tiempo de ejecución: {exec_time:.6f} segundos")
        print(f"Uso máximo de memoria: {mem_usage:.6f} MB")
        print("------------------------------------")

