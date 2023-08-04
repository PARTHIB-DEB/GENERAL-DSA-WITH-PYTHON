# This file represents Single Linked List dat structure with some other special ADDITION OF NODES only operations
'''
1) Insertion Before First Node
2) Insertion in between two Nodes
3) Insertion Before any location/Node (We have to declare external two markers to point the previous node, in short it is tending to be easy in Double LinkedList)
'''


class Node:
    def __init__(self) -> None:  # Class for Any Node Creation
        self._Value = None
        self._Next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.__head = Node()
        self.__size = 0

    def __NodeCreation(self) -> Node:
        newnode = Node()
        data = int(input("\n\t\tENTER DATA OF NODE:"))
        newnode._Value = data
        newnode._Next = None
        return newnode

    def InsertionBeforeFirstNode(self) -> None:
        if self.__size == 0:
            self.__head = self.__NodeCreation()
            print("\n\t\tFIRST NODE CREATED")
            self.__size += 1
        else:
            newnode = self.__NodeCreation()
            newnode._Next = self.__head
            self.__head = newnode
            self.__size += 1

    def InsertionBetweenNode(self) -> None:
        if self.__size == 0:
            self.__head = self.__NodeCreation()
            print("\n\t\tFIRST NODE CREATED")
            self.__size += 1
        else:
            newnode = self.__NodeCreation()
            n1 = int(input("\n\t\tENTER THE PRECEDING NODE:"))
            searchnode = self.__head
            if 0 < n1 <= self.__size:
                for i in range(1, self.__size+1):
                    if i == n1:
                        break
                    else:
                        searchnode = searchnode._Next
                newnode._Next = searchnode._Next
                searchnode._Next = newnode
                self.__size += 1
            else:
                print(f"\n\t\tGIVE A VALID NODE NUMBER")
                
                
    def displayList(self) -> None:
        search_node = self.__head
        print("\n\t\tLINKED-LIST:", end="\t")
        if self.__size == 0:
            print("Null")
        else:
            while (search_node != None):
                print(f"{search_node._Value}-->", end="\t")
                search_node = search_node._Next
            print("Null")


Obj_List = SingleLinkedList()
while (True):
    print("\n\t\t1 TO INSERT NEW NODE BEFORE A NODE \t\t 2 TO INSERT A NODE IN BETWEEN")
    Obj_List.displayList()
    op = int(input("\n\n\tOPERATION:"))
    match op:
        case 1:
            Obj_List.InsertionBeforeFirstNode()

        case 2:
            Obj_List.InsertionBetweenNode()

        case _:
            print("\n\n\t\tNO OPERATIONS MATCHED")
            break
