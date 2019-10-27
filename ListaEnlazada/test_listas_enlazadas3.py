from listas_enlazadas import Nodo, Linked_List , Linked_List_Tail

def main():
    lista = Linked_List()
    print(f"Esta vacia? : {lista.is_empty()}")
    lista.append(10)
    lista.append(20)
    lista.append(30)
    lista.append(40)
    lista.transversal()
    print(lista.get_tail().data)
    lista.transversal()
    lista.add_before(10,8)
    lista.transversal()
    lista.add_after(8,9)
    lista.transversal()
    lista.remove(1)
    lista.transversal()
    lista.remove(8)
    lista.transversal()
    print(lista.pop().data)
    lista.transversal()
    
main()
