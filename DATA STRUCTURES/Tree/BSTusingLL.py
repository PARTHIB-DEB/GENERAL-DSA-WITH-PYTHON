'''
1) Its a Binary Tree , so Probaility of having child node of a particular node is 0 or 1 or 2
2) Here, if the new childNode's value is greater than the current root then , root.rightSide=childNode else root.leftSide=childNode
3) So here is the Pseudocode -
    
    if RootNode is not None:
        childNode()
        if childNode.value > RootNode.value:
            if rootNode.right is not None:
                Insert childNode at RIGHTSIDE of RootNode
            else:
                RootNode=rootNode.right
        else:
            if rootNode.left is not None:
                Insert childNode at LEFTSIDE of RootNode
            else:
                RootNode=rootNode.left
    else:
        RootNode()
'''
class Node:  # Its a class which will create a new node object whenever called
    def __init__(self) -> None:
        self._Value = None
        self._Next = None
        self._Prev = None

class BSTbyLL:
    def __init__(self) -> None:
        self.__rootNode = None
        self.__listsize = 0
    
    def __NodeCreation(self) -> Node:
        newnode = Node()
        data = int(input("\n\t\tENTER DATA OF NODE:"))
        newnode._Value = data
        return newnode
    
    def insert(self)->None:
        if self.__rootNode is not None:
            childNode=self.__NodeCreation()
            if childNode._Value > self.__rootNode._Value:
                if self.__rootNode._Next is not None:
                    self.__rootNode._Next=childNode
                    self.__listsize+=1
                else:
                    self.__rootNode=self.__rootNode._Next
            else:
                if self.__rootNode._Prev is not None:
                    self.__rootNode._Prev=childNode
                    self.__listsize+=1
                else:
                    self.__rootNode=self.__rootNode._Prev
        else:
            self.__rootNode=self.__NodeCreation()
            self.__listsize+=1
    
    def displayList(self):
        if self.__listsize>0:
            search_node=self.__rootNode
            print("\n\t\tBST:",end="\t")
            while(search_node!= None):
                print(f"{search_node._Value}-->",end="\t")
                search_node=search_node._Next
            print("Null")
        else:
            print("\n\t\t NOTHING TO SHOW")

obj=BSTbyLL()
while(1):
    obj.displayList()
    op=int(input("\n\tPRESS 1 TO INSERT ONLY:"))
    match op:
        case 1:
            obj.insert()
            print("\n\t\tNODE INSERTED SUCCESSFULLY")
        case _:
            print("\n\t\tWRONG OPTION")