# This Program shows how to make a tree using a linear continuous memory based DS - List(Representating array here)
'''
while Creating TREE using array ,  we have to remind that:
1) Child Node of a node at location 'x' will be either in (2*x+1) or (2*x-1)
2) Maybe some of the memeory address in a list maybe empty as we know that in each level of tree, its not a must to have same no of child nodes for all parent node
'''
class TreeByList:
    def __init__(self,size,root_val) -> None:
        '''
            1) Fill value in the root index
            2) Give choice to user that either 1 or 2 as how many child index it have empty
            3) If user have filled one child , ask again if he/she want to fill another one or not
            else
            4) Give user an option: either 1 or 2 whom he/she will make as new root index and back to step-1
        '''
        self.size=size
        self.root=0
        self.treelist={}
        self.treelist[self.root]=root_val
    
    
    def display(self):
        for i in self.treelist.keys():
            print(f"\n\t\tARR[{i}]:{self.treelist[i]}")
        print("\n")     
    
    
    def fill_tree(self) -> None:
        while(self.root*2<=self.size-1):
            self.display()
            print(f"\n\t\t 1 TO CHOOSE LEFT CHILD OF {self.root} \t\t 2 TO CHOOSE RIGHT CHILD OF {self.root}\n")
            choice=int(input("\n\t\t WHICH CHILD IS NEXT ROOT:"))
            if choice == 1:
                left_child=2*self.root+1
                print(f"\n\t\tNOW ROOT AT {left_child} , LEFT CHILD OF {self.root}")
                self.root=left_child
                self.treelist[self.root]=int(input(f"\n\t\t VALUE OF NODE AT {self.root} :"))
            elif choice == 2:
                right_child=2*self.root+2
                print(f"\n\t\tNOW ROOT AT {right_child} , LEFT CHILD OF {self.root}")
                self.root=right_child
                self.treelist[self.root]=int(input(f"\n\t\t VALUE OF NODE AT {self.root} :"))
            else:
                print("\n\t\t WRONG CHOICE")
                break
        else:
            print(f"\n\t\tTREE FILLED")
            self.display()  

obj=TreeByList(int(input("\n\t\t SIZE:")),int(input("\n\t\t VALUE AT INDEX 0:")))
obj.fill_tree()
                

