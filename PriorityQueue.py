# This file represents a basic definition of a Priority-Queue and some operations related to it
# Linear-Queue is a linear data structure , but like DEqueue , it also does not follow FIFO rule.
# Here Items are placed according to their priority
# Here I am using List as the container
'''
Operarions : 1) Manipulative : Insertion ,  Deletion
             2) Checking : Front,End, size_Queue & is_empty
'''


class MyQueue:
    def __init__(self, totalsize) -> None:
        self.__front = 0 # Its constant , because actual deletion is happening here, no need to increment
        self.__end = -1
        self.__Queue = []
        self.__totalsize = totalsize
        self.__max_priority=0

    def Queue_filled_unfilled(self) -> int:
        if self.__end > -1:
            filled = self.__end
        else:
            filled = self.__end +1
        print(f"\n\t\t FILLED : {filled} AND UNFILLED : {self.__totalsize - filled}")
        
    

    def enqueue(self) -> None:
        if self.__end == -1:
            self.__end = 0
        if self.__end == self.__totalsize :
            print("\n\t\tQUEUE IS FULL , NOTHING TO INSERT")
        else:
            data=int(input("\n\t\t ENTER DATA :"))
            pr=int(input("\n\t\tENTER PRIORITY:"))
            print(f"\n\t\tNOW MAX PRIORITY:{self.__max_priority}")
            if pr >= self.__max_priority: # PLACING PRIORITY WISE INTERNAL SORTING
                self.__max_priority=pr
                self.__Queue.insert(self.__end,data)
                print(f"\n\t\t{data} IS INSERTED SUCCESSFULLY!!")
                self.__end=self.__end+1
            else:
                self.__Queue.insert(self.__front,data)
                print(f"\n\t\t{data} IS INSERTED SUCCESSFULLY!!")
                self.__end=self.__end+1
        
    def dequeue(self) -> None: # Here as actual deletion is happening , so No need to increment 'front'
        try:
            data=self.__Queue[self.__front]
            print(f"\n\t\t VALUE : {data} IS DELETED FROM {self.__front}")
            self.__Queue.remove(data)
        except Exception:
            print("\n\t\t ALL ELEMENTS ARE DELETED")
        

    def display(self) -> None: # As front marker is constant , so it will print automatically print empty / filled queue
        for i in range(len(self.__Queue)):
            print(f"\n\t\tQUEUE[{i}]={self.__Queue[i]}")

Queue_Obj = MyQueue(int(input("\n\t QUEUE SIZE:")))
while (True):
    print("\n")
    print("\t\t1 TO STATE OF QUEUE \n\t\t 2 TO INSERT_VALUE \t\t 3 TO DELETE_VALUE")
    print("\n")
    Queue_Obj.display()
    op = int(input("\n\tOPERATION:"))
    match op:
        case 1:
            Queue_Obj.Queue_filled_unfilled()

        case 2:
            Queue_Obj.enqueue()

        case 3:
            Queue_Obj.dequeue()

        case _:
            print("\n\n\t\tNO OPERATIONS MATCHED")
            break
