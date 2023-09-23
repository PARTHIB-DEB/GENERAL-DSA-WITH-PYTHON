def traversal(n,beg,aux,end):
    if n<=0:
        print("\n\t\t Illegal Move")
    elif n==1:
        print("\n\t\t Moving From %c to %c" %(beg,end))
    else:
        traversal(n-1,beg,end,aux)
        traversal(1,beg,aux,end)
        traversal(n-1,aux,beg,end)

traversal(3,"A","B","C")