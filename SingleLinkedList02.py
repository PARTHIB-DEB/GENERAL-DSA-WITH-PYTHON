# This file represents Single Linked List dat structure with some other special ADDITION OF NODES only operations
'''
1) Addition Before a Node
2) Addition in between two Nodes
3) Addition Before a location
4) Addition after a location
'''

# This is another Way Of creating any Linkedlist, Here We have taken the Value of Head_Node from Out of the Class, and have not taken the help of list_size
# In short , this is the most common approach of creating a linkedlist in any language
class Node:
    def __init__(self) -> None: # Class for Any Node Creation
        self._Value=None
        self._Next=None
    
class SingleLinkedList:
    def __init__(self,Head) -> None:
        self.__head=Head
    
    def firstNodeCreation(self,data) ->Node:
        newnode=Node()
        newnode._Value=data
        return newnode
    
    def InsertionBeforeNode(self,data)->None:
        if self.__head is None:
            value=data
            print(f"\n\t\tFIRST NODE CREATED")
            self.__head = self.firstNodeCreation(value)
        else:
            newnode=Node()
            newnode._Value=data
            newnode._Next=self.__head
            self.__head=newnode
            
    def InsertionBetweenNode(self,data,n1)->None:
        count=0
        if self.__head is None:
            value=data
            print(f"\n\t\tFIRST NODE CREATED")
            self.__head = self.firstNodeCreation(value)
        else:
            newnode=Node()
            newnode._Value=data
            searchnode=self.__head
            while searchnode._Next is not None:
                count += 1
                if count == n1:
                    break
                else:
                    searchnode=searchnode._Next
            newnode._Next=searchnode._Next
            searchnode._Next=newnode
            
                
        
    
    def displayList(self) -> None:
        search_node=self.__head
        print("\n\t\tLINKED-LIST:",end="\t")
        while(search_node._Next!= None):
            print(f"{search_node._Value}-->",end="\t")
            search_node=search_node._Next
        print("Null")

Head_Node=Node()
Head_Node._Value=None
Obj_List=SingleLinkedList(Head_Node)
while(True):
    print("\n\t\t1 TO INSERT NEW NODE BEFORE A NODE \t\t 2 TO INSERT A NODE IN BETWEEN")
    Obj_List.displayList()
    op = int(input("\n\n\tOPERATION:"))
    match op:
        case 1:
            Obj_List.InsertionBeforeNode(int(input("\n\t\tENTER NEW NODE'S VALUE:")))
            print("\n")
            
        case 2:
            Obj_List.InsertionBetweenNode(int(input("\n\t\tENTER NEW NODE'S VALUE:")),int(input("\n\t\tENTER FIRST NODE:")))
            print("\n")
            
        case _:
            print("\n\n\t\tNO OPERATIONS MATCHED")
            break

    
    
        