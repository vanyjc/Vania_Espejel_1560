class Nodo:
    def __init__(self,value,siguiente = None):
        self.data=value
        self.next=siguiente

#ADT Linked List
class Linked_List:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def get_tail(self):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        return cur_node

    def append(self,value):
        if self.is_empty():
            self.head = Nodo(value)
        else:
            self.get_tail().next = Nodo(value)

    def prepend(self,value):
        self.head = Nodo(value,self.head)

    def transversal(self):
        cur_node = self.head
        while cur_node.next != None:
            print(cur_node.data,'->',end = '')
            cur_node = cur_node.next
        print(cur_node.data)

    def add_before(self,ref_value,value):
        cur_node = self.head
        prev = None
        while cur_node.data != ref_value:
            prev = cur_node
            cur_node = cur_node.next
        if prev == None:
            self.prepend(value)
        else:
            prev.next = Nodo(value)
            prev.next.next = cur_node

    def add_after( self , ref_value , value):
        cur_node=self.head
        sig = cur_node.next
        while cur_node.data != ref_value:
            cur_node = sig
            sig = cur_node.next
        cur_node.next = Nodo(value)
        cur_node.next.next = sig

    def remove( self, value ):
        cur_node = self.head
        try:
            previo = None
            while cur_node.data != value:
                previo = cur_node
                cur_node = cur_node.next
                pass
            if previo == None:
                self.head = cur_node.next
            else:
                previo.next = cur_node.next  
            pass
        except:
            print("El valor no se encuentra en la lista")
            pass
        pass

    def pop(self):
        cur_node = self.head
        while cur_node.next != None:
            prev = cur_node
            cur_node = cur_node.next
        prev.next = None
        return cur_node
        
        
class Linked_List_Tail:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def get_tail(self):
        return self.__tail

    def append(self,value):
        if self.is_empty():
            self.__head = self.__tail= Nodo(value)
        else:
            self.get_tail().next = Nodo(value)
            self.__tail=self.__tail.next
        self.__size+=1

    def transversal(self):
        current_node = self.__head
        while current_node.next != None:
            print(current_node.data,'->',end = '')
            current_node = current_node.next
        print(current_node.data)

    def prepend(self,value):
        self.__head = Nodo(value,self.__head)
        self.__size += 1

    def add_before(self,ref_value,value):
        cur_node = self.__head
        prev = None
        while cur_node.data != ref_value:
            prev = cur_node
            cur_node = cur_node.next
        if prev == None:
            self.prepend(value)
            self.__size+=1
        else:
            prev.next = Nodo(value)
            prev.next.next = cur_node
            self.size+=1

    def add_after( self , ref_value , value):
        cur_node=self.__head
        sig = cur_node.next
        while cur_node.data != ref_value:
            cur_node = sig
            sig = cur_node.next
        cur_node.next = Nodo(value)
        cur_node.next.next = sig
        self.size+=1

    def remove( self, value ):
        cur_node = self.__head
        try:
            previo = None
            while cur_node.data != value:
                previo = cur_node
                cur_node = cur_node.next
                pass
            if previo == None:
                self.__head = cur_node.next
                self.__size-=1
            else:
                previo.next = cur_node.next
                self.__size-=1
            pass
        except:
            print("El valor no se encuentra en la lista")
            pass
        pass

    def pop(self):
        cur_node = self.__head
        while cur_node.next != None:
            prev = cur_node
            cur_node = cur_node.next
        prev.next = None
        self.__size-=1
        return cur_node

        
    
