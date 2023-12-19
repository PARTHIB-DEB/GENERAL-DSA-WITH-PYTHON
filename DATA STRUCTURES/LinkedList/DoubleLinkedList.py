# This file represents Double Linked List data structure
# Double Linked List is basically a single linkedlist with bothway traversal

class Node:  # Its a class which will create a new node object whenever called
    def __init__(self) -> None:
        self._Value = None
        self._Next = None
        self._Prev = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.__head = Node()
        self.__listsize = 0
    
    def __NodeCreation(self) -> Node:
        newnode = Node()
        data = int(input("\n\t\tENTER DATA OF NODE:"))
        newnode._Value = data
        return newnode

    def InsertionAfterNode(self): # As here Insertion is happenning after the node having NONE at next, so don't need to make new node's next refrence as none
        if self.__listsize == 0:
            self.__head = self.__NodeCreation() # Creating The Head Node atfirst
            self.__listsize += 1
        else:
            newnode=self.__NodeCreation()
            search_node = self.__head
            while search_node._Next is not None:  # Traverse to the last node
                search_node = search_node._Next
            search_node._Next = newnode # Update the Next pointer of the last node
            newnode._Prev=search_node
            # newnode._Next = None  # Set the Next pointer of the new node to None
            self.__listsize += 1

    def DeletetionAfterHead(self):
        if self.__listsize>0:
            first_node=self.__head
            self.__head=first_node._Next
            # first_node._Next=None
            del first_node
            self.__listsize -=1
        else:
            print("\n\t\t NOTHING TO DELETE\n\n")
    
    def DeleteAtaLocation(self):
        if self.__listsize>0:
            i=1
            index=int(input("\n\t\t LOCATION OF NODE:"))
            if index>1:
                searchnode=self.__head
                prevnode=searchnode
                while i!=index:
                    prevnode=searchnode
                    searchnode=searchnode._Next
                    i+=1
                prevnode._Next=searchnode._Next
                searchnode._Prev=None
                searchnode._Next=None
                print(f"\n\t\t VALUE OF DEL NODE : {searchnode._Value}")
                # self.__listsize -=1
            else:
                self.DeletetionAfterHead()
        else:
            print("\n\t\t NOTHING TO DELETE\n\n")
        
    
    def displayList(self):
        if self.__listsize>0:
            search_node=self.__head
            print("\n\t\tLINKED-LIST:",end="\t")
            while(search_node!= None):
                print(f"{search_node._Value}-->",end="\t")
                search_node=search_node._Next
            print("Null")
        else:
            print("\n\t\t NOTHING TO SHOW")

Obj_List=DoubleLinkedList()
while(True):
    print("\n\t\t1 TO INSERT NODE \n\t\t 2 TO DELETE NODE \n\t\t 3 TO DELETE FROM A SPECIFIC POSITION")
    Obj_List.displayList()
    op = int(input("\n\n\tOPERATION:"))
    match op:
        case 1:
            Obj_List.InsertionAfterNode()
            print("\n")

        case 2:
            Obj_List.DeletetionAfterHead()
            print("\n")
            
        case 3:
            Obj_List.DeleteAtaLocation()
            
        case _:
            print("\n\n\t\tNO OPERATIONS MATCHED")
            break