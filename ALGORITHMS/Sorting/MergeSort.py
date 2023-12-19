# This File Contains about How to do Merge Sort in Python
# APart from Bubble,Insertion,selection sort, Merge sort is very less runtime taker because it applies divide and conquer algorithm
# Here as a mutable array we will take list DS

'''
Rules:
1) Search Mid value by applying Divide and conquer algo
2) From Mid , divide the total array into Two subarrays :Left and Right
3) Make sure that both subarrays are already sorted by any algo(If merge sort then It will be Recursive mergesort in whole)
4) After sorting, choose each elemnts from both subarrays , compare them , and put them in a 3rd array in correct order
'''

class MergeSort:
    def __init__(self,length) -> None:
        self.length=length
        self.arr=[]
        self.newarr=[]
    
    def fill_array(self)->None:
        arr_len=self.length
        for i in range(arr_len):
            self.arr.insert(i,int(input(f"\n\t\tARR[{i}]:")))
    
    
    def Sort_arr(self)->None:
        arr_len=self.length-1
        mid=(0+arr_len)//2
        left=self.arr[0:mid+1]
        left.sort() # Both The array Need to be sorted by any algo or builtimn fn
        right=self.arr[mid+1:len(self.arr)]
        right.sort() # Both The array Need to be sorted by any algo or builtimn fn
        print(f"\n\t\tBEFORE SORTING:{self.arr}")
        while(len(left)>0 and len(right)>0):
            if left[0]<right[0]:
                self.newarr.append(left[0])
                left.remove(left[0])
            else:
                self.newarr.append(right[0])
                right.remove(right[0])
        if len(left):
            self.newarr+=left
        if len(right):
            self.newarr+=right
        print(f"\n\t\tAFTER SORTING,ARR:{self.newarr}")           
        


obj=MergeSort(length=int(input("\n\t\tLENGTH:")))
obj.fill_array()
obj.Sort_arr()