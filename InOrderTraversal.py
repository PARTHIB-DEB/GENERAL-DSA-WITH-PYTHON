# This File Consists of Inorder Traversal of a tree
# For making of the tree we are taking List DS 
# Tree is a diagramatic representation of hiererchial Non-linear DS  
# So we will create a STATIC Tree in a LinkedList Manner
# InOrder Traversal : Left-Root-Right , specifically InOrder Traversal of a BST is a sorted array, because in BST root.left<root and root.right>root always

class Node:  # Its a class which will create a new node object whenever called
    def __init__(self,left=None,right=None,val=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.answer=[]

class InOrderTraversal:
    def Traversal(self,root:Node)->None:
        stack=[]
        self.answer=[]
        while(True):
            if root:
                stack.append(root)
                root=root.left
            else:
                if not stack:
                    break
                else:
                    root=stack.pop()
                    self.answer.append(root.val)
                    root=root.right
    
    def display(self)->None:
        print("\n\t\tIN-ORDER STACK:",end=" ")
        for i in range(len(self.answer)):
            print(f"{self.answer[i]}",end=" ")

root=Node(val=4)
root.left=Node(val=2)
root.right=Node(val=6)
root_left=root.left
root_right=root.right
root_left.left=Node(val=1)
root_left.right=Node(val=3)
root_right.left=Node(val=5)
root_right.right=Node(val=7)
obj=InOrderTraversal()
obj.Traversal(root=root)
obj.display()

