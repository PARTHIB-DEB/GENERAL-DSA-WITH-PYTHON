# This File Consists of Inorder Traversal of a tree
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
    '''
    InOrder says to traverse root.left-->root-->root.right , so as priority is starting from root.left
    so we have to traverse everytime to the left side of the current root and make it root untill root.left != Null
    that means everytime we are doing root=previous_root.left (root.left-->root)
    after that when root.left is Null , there is no more new root , so we search for existing root's right
    if existing root's right is not null , search for its left also , otherwise make root= current_root's ancestor (left ancestor)
    ------Upto all of these making root , will be done by poping the top element of the auxiliary stack and putting it in answer stack-----
    '''
    def Traversal(self,root:Node)->None:
        stack=[] # Similar to Recursive Stack
        self.answer=[] # Inorder Stack
        while(True):
            if root: # If root is not Null just put it in STACK and traverse Leftwise (as LEFT-->R-->RIGHT)
                stack.append(root)
                root=root.left
            else:
                if not stack: # STACK or auxuliary stack is empty means there is no root in tree , means empty tree
                    break
                else:
                    root=stack.pop() # Otherwise may be the new root (prev_root.left) is Null , so move to its rightside
                    self.answer.append(root.val)
                    root=root.right
        
        # return self.answer
    
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

