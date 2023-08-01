# This file represents a basic definition of a Double Ended - Queue and some operations related to it
# Double-Ended Queue (DEqueue) is basically a linear queue in which if one side is occupied for enqueue then another side must be for dequeue and vice-versa
# Basically a mixture of two linear queues in one linear
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

    def Queue_filled_unfilled(self) -> int:
        if self.__end > -1:
            filled = self.__end
        else:
            filled = self.__end +1
        print(f"\n\t\t FILLED : {filled} AND UNFILLED : {self.__totalsize - filled}")
        
    

    def enqueue_end(self) -> None:
        if self.__end == -1:
            self.__end = 0
        if self.__end == self.__totalsize :
            print("\n\t\tQUEUE IS FULL , NOTHING TO INSERT")
        else:
            data=int(input("\n\t\t ENTER DATA :"))
            self.__Queue.insert(self.__end,data)
            print(f"\n\t\t{data} IS INSERTED SUCCESSFULLY!!")
            self.__end=self.__end+1
        
    def dequeue_front(self) -> None: # Here as actual deletion is happening , so No need to increment 'front'
        try:
            data=self.__Queue[self.__front]
            print(f"\n\t\t VALUE : {data} IS DELETED FROM {self.__front}")
            self.__Queue.remove(data)
        except Exception:
            print("\n\t\t ALL ELEMENTS ARE DELETED")
            
    def enqueue_front(self) -> None:
        if self.__end == -1:
            self.__end = 0
        if self.__end == self.__totalsize :
            print("\n\t\tQUEUE IS FULL , NOTHING TO INSERT")
        else:
            data=int(input("\n\t\t ENTER DATA :"))
            self.__Queue.insert(self.__front,data)
            print(f"\n\t\t{data} IS INSERTED SUCCESSFULLY!!")
            self.__end=self.__end+1
        
    def dequeue_end(self) -> None: # Here as actual deletion is happening , so No need to increment 'front'
        try:
            self.__end-=1
            data=self.__Queue[self.__end]
            print(f"\n\t\t VALUE : {data} IS DELETED FROM {self.__end}")
            self.__Queue.remove(data)
        except Exception:
            print("\n\t\t ALL ELEMENTS ARE DELETED")
        

    def display(self) -> None: # As front marker is constant , so it will print automatically print empty / filled queue
        print(f"\n\t\tQUEUE : {self.__Queue}")

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
            print("\t\t \"ene\" TO INSERT FROM END \n\t\t \"def\" TO DELETE FROM FRONT")
            option=input("\n\t\tENQUEUE BY END or DEQUEUE BY FRONT??-->")
            if option == "ene":
                Queue_Obj.enqueue_end()
            elif option == "def":
                Queue_Obj.dequeue_front()
            else:
                print("\n\t\tNO OPTIONS MATCHED")

        case 3:
            print("\t\t \"enf\" TO INSERT FROM FRONT \n\t\t \"dee\" TO DELETE FROM END")
            option=input("\n\t\tENQUEUE BY FRONT or DEQUEUE BY END??-->")
            if option == "enf":
                Queue_Obj.enqueue_front()
            elif option == "dee":
                Queue_Obj.dequeue_end()
            else:
                print("\n\t\tNO OPTIONS MATCHED")


        case _:
            print("\n\n\t\tNO OPERATIONS MATCHED")
            break
