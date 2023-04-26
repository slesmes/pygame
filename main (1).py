from single_linked_list import SingleLinkedList
inst_sll = SingleLinkedList()

# Ingresamos como parametro el valor del nodo

""" Métodos para añadir nodo """
inst_sll.create_node_sll_ends("Batman")
inst_sll.create_node_sll_ends('Robin')
inst_sll.create_node_sll_ends('Gatubela')
inst_sll.create_node_sll_ends('Deadpool')
inst_sll.create_node_sll_ends('Ant Man')
inst_sll.create_node_sll_ends('Flecha')
inst_sll.create_node_sll_ends("Wolverine")
inst_sll.create_node_sll_unshift("Hulk")

# | Hulk | Batman | Robin | Wolverine
inst_sll.show_list()

""" Métodos de eliminar """
print('---------------------------------------------------')
print('     >> Eliminar último nodo <<')
inst_sll.delete_node_sll_pop()
inst_sll.show_list()

# | Hulk | Batman | Robin |

print('---------------------------------------------------')
print('\n     >> Eliminar primer nodo <<')
inst_sll.shift_node_sll()
inst_sll.show_list()
# | Batman | Robin |

print('---------------------------------------------------')
print('\n     >> Consultar valor de nodo <<')
inst_sll.get_node_value(1)
inst_sll.get_node_value(2)

print('---------------------------------------------------')
print('\n     >> Actualizar valor de nodo <<')
inst_sll.update_node_value(1, "Linterna verde")
inst_sll.show_list()

print('---------------------------------------------------')
print('\n     >> Eliminar nodo expecifico<<')
inst_sll.remove_node(3)
inst_sll.show_list()


print('---------------------------------------------------')
print('\n           >>Tamaño de la SLL<<')
inst_sll.show_SLL_length()

print('---------------------------------------------------')
print('\n           >>Buscar un elemento y devolver su posicion<<')
inst_sll.search_an_element_and_return_index('Deadpool')

print('---------------------------------------------------')
print('\n               >>Lista Invertida<<')
inst_sll.reverse()
inst_sll.show_list()

print('---------------------------------------------------')
print('\n               >>Lista ordenada<<')
inst_sll.sort_all_elements()
inst_sll.show_list()

print('---------------------------------------------------')
print('\n               >>Insertar Elemento<<')
inst_sll.insert_an_element_in_an_specific_index(2,'Spider Man')
inst_sll.show_list()

print('---------------------------------------------------')
print('\n               >>Lista Eliminada<<')
inst_sll.eliminate_all_elements()
inst_sll.show_list()

print('---------------------------------------------------')
print('\n               >>Verificar Lista Eliminada<<')
inst_sll.empty_list()
inst_sll.show_list()

