# This File Contains about How to do Insertion Sort imn Python
# After Bubble Sort, Insertion sort is the most similar , yet a little runtime taker
# Here as a mutable array we will take list DS

class InsertionSort:
    def __init__(self,length) -> None:
        self.length=length
        self.arr=[]
    
    def fill_array(self)->None:
        arr_len=self.length
        for i in range(arr_len):
            self.arr.insert(i,int(input(f"\n\t\tARR[{i}]:")))
    
    def Sort_arr(self)->None:
        arr_len=self.length
        for i in range(1,len(self.arr)):
            key=self.arr[i]
            j=i-1
            while (j>=0 and self.arr[j]>key):
                self.arr[j+1]=self.arr[j]
                # print(f"\n\t\tARR:{self.arr}") # Uncomment If you want to see the steps
                j-=1
            self.arr[j+1]=key
        print(f"\n\t\tAFTER SORTING,ARR:{self.arr}")


obj=InsertionSort(length=int(input("\n\t\tLENGTH:")))
obj.fill_array()
obj.Sort_arr()