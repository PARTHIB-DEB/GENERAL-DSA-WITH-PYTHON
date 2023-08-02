# Linkedlist is a Linear , NON-PRIMITIVE data structure
# There are 3 types of linkedlist -> 1) Single 2) Circular 3) Double
# Eventhough the terminologies are same like the terms used in Queues , all 3 linkedlist are seperated according to their ways of traversals
# Whereas In queues, its the way of insertion(enqueue) and deletion(dequeue)
# This file represents Single Linked List dat structure

#Funfact : This is also LINEAR-QUEUE representation by SINGLELINKEDLIST

class Node:  # Its a class which will create a new node object whenever called
    def __init__(self) -> None:
        self._Value = None
        self._Next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.__head = Node()  # Here SingleLinkedList class has not inherited Node class because , Inheritance doesnot allow you to change parent class's value by Child Class
                              # whenever we call the SingleLinkedList we automatically create a Head Node (along with its size)
        self.__listsize = 0

    def InsertionAfterNode(self, value): # As here Insertion is happenning after the node having NONE at next, so don't need to make new node's next refrence as none
        newnode = Node()
        newnode._Value = value
        if self.__listsize == 0:
            self.__head = newnode
            # self.__head._Next = None
            self.__listsize += 1
        else:
            search_node = self.__head
            while search_node._Next is not None:  # Traverse to the last node
                search_node = search_node._Next
            search_node._Next = newnode  # Update the Next pointer of the last node
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
            print("\n\t\t NOTHING TO DELETE")
        
    
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

Obj_List=SingleLinkedList()
while(True):
    print("\t\t1 TO INSERT NODE \n\t\t 2 TO DELETE NODE")
    Obj_List.displayList()
    op = int(input("\n\n\tOPERATION:"))
    match op:
        case 1:
            Obj_List.InsertionAfterNode(int(input("\n\t\tENTER NEW NODE'S VALUE:")))
            print("\n")

        case 2:
            Obj_List.DeletetionAfterHead()
            
        case _:
            print("\n\n\t\tNO OPERATIONS MATCHED")
            break


    
    
        