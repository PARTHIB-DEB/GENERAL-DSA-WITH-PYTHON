# This file represents a basic definition of a stack and some operations related to it
# Stack is a linear data structure , means having continuous memory allocation of elements inside a block
# Here I am using List as the container 
'''
Operarions : 1) Manipulative : Push, Pop
             2) Checking : Top value, size_stack & is_empty
'''


class Mystack:
    def __init__(self, totalsize) -> None:
        self.__top = -1
        self.__stack = []
        self.__totalsize = totalsize

    def is_empty(self) -> int:
        if self.__top == -1:
            return 0
        return 1

    def is_full(self) -> int:
        if self.__top == self.__totalsize - 1:
            return 0
        return 1

    def top_value(self) -> int:
        if self.is_empty() == 0:
            return 'NOTHING'
        return self.__stack[self.__top]
    
    def stack_filled(self) -> None:
        print(f"\n\t\tSIZE OF STACK IS :{self.__top + 1}")

    def insertion(self) -> None:
        if self.is_full() != 0:
            self.__top += 1
            value=int(input("\n\t\tENTER VALUE TO INSERT:"))
            self.__stack.insert(self.__top, value)
            print(f"\n\t\tVALUE {value} IS INSERTED AT {self.__top}")
        else:
            print("\n\t\tSTACK IS FULL")
    
    def deletion(self)->None:
        if self.is_empty() != 0:
            Item_to_delete=self.__stack[self.__top]
            self.__stack.remove(Item_to_delete)
            print(f"\n\t\tValue : {Item_to_delete} is deleted from Index {self.__top}")
            self.__top-=1
        else:
            print("\n\n\t\tSTACK IS EMPTY")
    
    def display(self) -> None:
        if self.is_empty()==0:
            print("\n\t\tNOTHING TO DISPLAY")
        else:
            print(f"\n\t\tSTACK : {self.__stack} ")

Stack_Obj=Mystack(int(input("\n\t STACK SIZE:")))
while(True):
    print("\n")
    print("\t\t1 TO HOW_MUCH_FILLED \t\t 2 TO CHECK_VALUE_AT_TOP \n\t\t 3 TO INSERT_VALUE \t\t 4 TO DELETE_VALUE")
    print("\n")
    Stack_Obj.display()
    op=int(input("\n\tOPERATION:"))
    match op:
        case 1:
            Stack_Obj.stack_filled()

        case 2:
            print(f"\n\n\t\tVALUE AT THE TOP OF THE STACK :{Stack_Obj.top_value()}")

        case 3:
            Stack_Obj.insertion()

        case 4:
            Stack_Obj.deletion()

        case _:
            print("\n\n\t\tNO OPERATIONS MATCHED")
            break



