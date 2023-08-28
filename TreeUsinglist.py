# This Program shows how to make a tree using a linear continuous memory based DS - List(Representating array here)
'''
while Creating TREE using array ,  we have to remind that:
1) Child Node of a node at location 'x' will be either in (2*x+1) or (2*x-1)
2) Maybe some of the memeory address in a list maybe empty as we know that in each level of tree, its not a must to have same no of child nodes for all parent node
'''
class TreeByList:
    def __init__(self,size) -> None:
        '''
            1) Make the current index root
            2) Give choice to user that either 1 or 2 as how many child index it have empty
            3) If user have filled one child , ask again if he/she want to fill another one or not
            else
            4) Give user an option: either 1 or 2 whom he/she will make as new root index and back to step-1
        '''
        self.size=size
        self.root=0
        self.treelist=[None]
    
    def fill_tree(self) -> None:
        value=int(input("\n\t\t Node's Value:"))
        self.treelist[self.root]=value
        child_node_list=[self.root*2+1,self.root*2+2]
        print("\n\t\tPRESS 1 FOR LEFT_CHILD \t\t 2 FOR RIGHT_CHILD\n")
        child_choice=int(input("\n\t\tWHICH CHILD:"))
        match(child_choice):
            case 1:
                self.root=child_node_list[0]
                print("LEFT CHILD IS NEW ROOT NODE")
            case 2:
                self.root=child_node_list[1]
                print("RIGHT CHILD IS NEW ROOT NODE")
            case _:
                print("\n\t\t SETING LEFT CHILD AS DEFAULT\n")

