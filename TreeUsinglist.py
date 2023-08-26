# This Program shows how to make a tree using a linear continuous memory based DS - List(Representating array here)
'''
while Creating TREE using array ,  we have to remind that:
1) Child Node of a node at location 'x' will be either in (2*x+1) or (2*x-1)
2) Maybe some of the memeory address in a list maybe empty as we know that in each level of tree, its not a must to have same no of child nodes for all parent node
'''
class TreeByList:
    def __init__(self,size) -> None:
        self.size=size
        self.root=0
        self.treelist=[None]
    
    def fill_tree(self) -> None:
        j=1
        while self.root<=self.size-1:
            '''
            1) Make the current index root
            2) Give choice to user that either 1 or 2 as how many child index it have empty
            3) If user have filled one child , ask again if he/she want to fill another one or not
            else
            4) Give user an option: either 1 or 2 whom he/she will make as new root index and back to step-1
            '''
            # choice=int(input("\n\t\t ENTER YOUR CHOICE:"))
            # match(choice):
            #     case 1:
            #         if self.treelist[self.root]==None:
            #             value=int(input(f"\n\t\tENTER VALUE AT NODE {self.root}: "))
            #             self.treelist.insert(self.root,value)
            #             leftchild=2*self.root+1
            #             rightchild=2*self.root+2
            #             if leftchild<=self.size-1:
            #                 self.treelist.insert(leftchild,None)
            #             if rightchild<=self.size-1:
            #                 self.treelist.insert(rightchild,None)
            #         else:
            #             print("\n\t\tNOT EMPTY")
            #             continue
                