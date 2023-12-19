# This file represents Circular Linked List dat structure

class Node:  # Its a class which will create a new node object whenever called
    def __init__(self) -> None:
        self._Value = None
        self._Next = None


class CircularLinkedList:
    def __init__(self) -> None:
        self.__head = Node()
        self.__listsize = 0
    
    def __NodeCreation(self) -> Node:
        newnode = Node()
        data = int(input("\n\t\tENTER DATA OF NODE:"))
        newnode._Value = data
        newnode._Next = None
        return newnode

    def InsertionAfterNode(self): # As here Insertion is happenning after the node having NONE at next, so don't need to make new node's next refrence as none
        if self.__listsize == 0:
            self.__head = self.__NodeCreation() # Creating The Head Node atfirst
            self.__head._Next = self.__head
            self.__listsize += 1
        else:
            search_node = self.__head
            newnode=self.__NodeCreation()
            while search_node._Next is not self.__head:  
                search_node = search_node._Next
            search_node._Next = newnode  # Update the Next pointer of the last node
            newnode._Next = self.__head  # Set the Next pointer of the new node to head
            self.__listsize += 1

    def DeletetionAfterHead(self):
        if self.__listsize>0:
            search_node=self.__head
            temp=self.__head
            while (search_node._Next is not self.__head):
                search_node=search_node._Next
            self.__head=self.__head._Next # Incrementing head
            search_node._Next=self.__head # Making the last node's next 
            print(f"\n\t\tHEAD NODE OF VAL {temp._Value} IS DELETED")
            self.__listsize-=1
        else:
            print("\n\t\tNOTHING TO DELETE")
        
    
    def displayList(self):
        if self.__listsize>0:
            search_node=self.__head
            print(f"\n\t\tLINKED-LIST:\t{search_node._Value}-->",end="\t")
            search_node=search_node._Next
            while(search_node!= self.__head):
                print(f"{search_node._Value}-->",end="\t")
                search_node=search_node._Next
            print("Null")
        else:
            print("\n\t\t NOTHING TO SHOW")

Obj_List=CircularLinkedList()
while(True):
    print("\n\t\t1 TO INSERT NODE \n\t\t 2 TO DELETE NODE")
    print("\n")
    Obj_List.displayList()
    op = int(input("\n\n\tOPERATION:"))
    match op:
        case 1:
            Obj_List.InsertionAfterNode()
            print("\n")

        case 2:
            Obj_List.DeletetionAfterHead()
            
        case _:
            print("\n\n\t\tNO OPERATIONS MATCHED")
            break


    
    
        