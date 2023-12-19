# This File Consists of Preorder Traversal of a tree 
# Tree is a diagramatic representation of hiererchial Non-linear DS  
# So we will create a STATIC Tree in a LinkedList Manner
# InOrder Traversal : Left-Root-Right , specifically InOrder Traversal of a BST is a sorted array, because in BST root.left<root and root.right>root always

class Node:  # Its a class which will create a new node object whenever called
    def __init__(self,left=None,right=None,val=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.answer=[]

class PreOrderTraversal:
    def Traversal(self,root:Node)->None:
        '''
        PreOrder says to traverse ROOT--->LEFT--->RIGHT, that means first of all we have to prirotize the root node
        Now how to traverse!!-- As we are using STACK as auxiliary space and It follows LIFO principle so inorder to get
        nodes in LEFT-->RIGHT manner in the answer , we have to push the root.right atfirst in AUXILIARY STACK then root.left 
        that make sense when we are trying to pop out from stack (root.left will emit first)
        ----Here popping will not be done based on checking 'Null is there or not' condition, after simultaneous pushing, 
        we have to pop the root.left asusual and then root.right----
        '''
        stack=[] # Similar to Recursive Stack
        self.answer=[] # Preorder stack
        if not root: # as the auxiliary STACK must have the topmost ROOT before traversal, so this checking is done primarily
            return
        else:
            stack.append(root)
        while(len(stack)>0):
            root=stack.pop() # Now we are doing operations by taking the top-root from aux stack and pushing it in answer
            self.answer.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
                
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
obj=PreOrderTraversal()
obj.Traversal(root=root)
obj.display()

