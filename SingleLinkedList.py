# Linkedlist is a Linear , NON-PRIMITIVE data structure
# There are 3 types of linkedlist -> 1) Single 2) Circular 3) Double
# Eventhough the terminologies are same like the terms used in Queues , all 3 linkedlist are seperated according to their ways of traversals
# Whereas In queues, its the way of insertion(enqueue) and deletion(dequeue)
# This file represents Single Linked List dat structure

class Node: # Its a class which will create a new node object whenever called
    def __init__(self) -> None:
        self._value=None
        self._NextPtr=None
class SingleLinkedList:
    def __init__(self) -> None:
        self.__newnode=Node() # Here SingleLinkedList class has not inherited Node class because , Inheritance doesnot allow you to change parent class's value by Child Class
        self.__size=0
        
        #To be Continued....