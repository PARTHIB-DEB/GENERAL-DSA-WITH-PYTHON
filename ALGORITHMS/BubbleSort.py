# This File Contains about How to do Bubble Sort imn Python
# Bubble Sort is the most Primitive Way to perform sorting an mutable array in any language
# Although there is a built-in sort() method in python , we will comparfe it's runtime to bubble sort's runtime
# Here as a mutable array we will take list DS

class BubbleSort:
    def __init__(self,length) -> None:
        self.length=length
        self.arr=[]
    
    def fill_array(self)->None:
        arr_len=self.length
        for i in range(arr_len):
            self.arr.insert(i,int(input(f"\n\t\tARR[{i}]:")))
    
    def Sort_arr(self)->None:
        arr_len=self.length
        for i in range(arr_len-1): #Passes
            for j in range(arr_len-i-1): #rotations
                if self.arr[j]>self.arr[j+1]:
                    self.arr[j],self.arr[j+1]=self.arr[j+1],self.arr[j]
                # print(f"\n\t\tARR:{self.arr}")
        print(f"\n\t\tAFTER SORTING,ARR:{self.arr}")


obj=BubbleSort(length=int(input("\n\t\tLENGTH:")))
obj.fill_array()
obj.Sort_arr()