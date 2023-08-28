# This Program shows how to make a tree using a linear continuous memory based DS - List(Representating array here)
'''
while Creating TREE using array ,  we have to remind that:
1) Child Node of a node at location 'x' will be either in (2*x+1) or (2*x-1)
2) Maybe some of the memeory address in a list maybe empty as we know that in each level of tree, its not a must to have same no of child nodes for all parent node
'''
class TreeByList:
    def __init__(self,size) -> None:
        '''
            1) Fill value in the root index
            2) Give choice to user that either 1 or 2 as how many child index it have empty
            3) If user have filled one child , ask again if he/she want to fill another one or not
            else
            4) Give user an option: either 1 or 2 whom he/she will make as new root index and back to step-1
        '''
        self.size=size
        self.root=0
        self.treelist=[None]
    
    
    def display(self):
        for i in range(len(self.treelist)):
            if str(self.treelist[i]).isdigit():
                print(f"\n\t\tARR[{i}]:{self.treelist[i]}")
            else:
                print("\n\n\t\tNone",end="\t")
        print("\n")
            
    
    
    def fill_tree(self) -> None:
        while(len(self.treelist)<=self.size):
            self.display()
            value=int(input("\n\t\t Node's Value:"))
            if self.root == 0:
                self.treelist.insert(self.root,value)
                child_choice=int(input("\n\t\tWHICH CHILD IS NEW ROOT:"))
                if child_choice == 1:
                    self.root=2*self.root + 1
                    if self.root <= self.size -1 :
                        if str(self.treelist[self.root]).isdigit():
                            print("\n\n\t\tNODE IS FILLED ALREADY")
                            continue
                        else:
                            in_hand_node=self.root+1
                            continue
                    else:
                        print("\n\n\t\t OUT OF LIST")
                        continue
                elif child_choice == 2 :
                    self.root=2*self.root + 2
                    if self.root <= self.size -1 :
                        if str(self.treelist[self.root]).isdigit():
                            print("\n\n\t\tNODE IS FILLED ALREADY")
                            continue
                        else:
                            in_hand_node=self.root-1
                            continue
                    else:
                        print("\n\n\t\t OUT OF LIST")
                        continue  
            else:
                print("\n\t\tPRESS 1 FOR PREVIOUS NODE \t\t 2 FOR NEW CHILD NODE")
                match(int(input("\n\t\t PREVIOUS OR NEW ROOT:"))):
                    case 1:
                        self.treelist.insert(in_hand_node,value)
                    case 2:
                        child_choice=int(input("\n\t\tWHICH CHILD IS NEW ROOT:"))
                        if child_choice == 1:
                            try:
                                self.root=2*self.root + 1
                                if self.root <= self.size -1 :
                                    if str(self.treelist[self.root]).isdigit():
                                        print("\n\n\t\tNODE IS FILLED ALREADY")
                                        continue
                                    else:
                                        in_hand_node=self.root+1
                                        continue
                            except Exception:
                                print("\n\n\t\t OUT OF LIST")
                                continue
                        elif child_choice == 2 :
                            try:
                                self.root=2*self.root + 2
                                if self.root <= self.size -1 :
                                    if str(self.treelist[self.root]).isdigit():
                                        print("\n\n\t\tNODE IS FILLED ALREADY")
                                        continue
                                    else:
                                        in_hand_node=self.root-1
                                    continue
                            except Exception:
                                print("\n\n\t\t OUT OF LIST")
                                continue         
                            

obj=TreeByList(5)
obj.fill_tree()
                

