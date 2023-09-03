# This file represents Double Linked List data structure
# Double Linked List is basically a single linkedlist with bothway traversal

class Node:  # Its a class which will create a new node object whenever called
    def __init__(self) -> None:
        self._Value = None
        self._Next = None
        self._Prev = None


class TreeByLL:
    def __init__(self) -> None:
        self.__head = Node()
        self.__listsize = 0
    
    def __NodeCreation(self) -> Node:
        newnode = Node()
        data = int(input("\n\t\tENTER DATA OF NODE:"))
        newnode._Value = data
        return newnode

    def InsertionAtLeft(self): # As here Insertion is happenning after the node having NONE at next, so don't need to make new node's next refrence as none
        if self.__listsize == 0:
            self.__head = self.__NodeCreation() # Creating The Head Node atfirst
            self.__listsize += 1
        else:
            nodeNo=int(input("\n\t\t NODE NO:"))
            search_node = self.__head
            i=0
            while (i<=nodeNo):
                search_node=search_node._Next
                i+=1
            if search_node._Prev == None:
                newnode=self.__NodeCreation()
                search_node._Prev=newnode
                newnode._Next=search_node
                self.__listsize += 1
            else:
                print("\n\t\t ALREADY HAS A NODE")
            
    def InsertionAtRight(self): # As here Insertion is happenning after the node having NONE at next, so don't need to make new node's next refrence as none
        if self.__listsize == 0:
            self.__head = self.__NodeCreation() # Creating The Head Node atfirst
            self.__listsize += 1
        else:
            nodeNo=int(input("\n\t\t NODE NO:"))
            search_node = self.__head
            i=0
            while (i<=nodeNo):
                search_node=search_node._Next
                i+=1
            if search_node._Next == None:
                newnode=self.__NodeCreation()
                search_node._Next=newnode
                newnode._Prev=search_node
                self.__listsize += 1
            else:
                print("\n\t\t ALREADY HAS A NODE")
        
    
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

Obj_List=TreeByLL()
while(True):
    print("\n\t\t1 TO INSERT NODE AT LEFT \n\t\t 2 TO INSERT NODE AT RIGHT ")
    Obj_List.displayList()
    op = int(input("\n\n\tOPERATION:"))
    match op:
        case 1:
            Obj_List.InsertionAtLeft()
            print("\n")

        case 2:
            Obj_List.InsertionAtRight()
            print("\n")
            
        case _:
            print("\n\n\t\tNO OPERATIONS MATCHED")
            break