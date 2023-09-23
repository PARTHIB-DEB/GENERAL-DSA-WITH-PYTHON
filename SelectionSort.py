# This File Contains about How to do Selection Sort imn Python
# Here as a mutable array we will take list DS

class SelectionSort:
    def __init__(self,length) -> None:
        self.length=length
        self.arr=[]
    
    def fill_array(self)->None:
        arr_len=self.length
        for i in range(arr_len):
            self.arr.insert(i,int(input(f"\n\t\tARR[{i}]:")))
    
    def Sort_arr(self)->None:
        flag=0
        arr_len=self.length
        for i in range(len(self.arr)-1): #Passess
            min_index=i
            for j in range(i+1,len(self.arr)): # Comparison for finding most minimum term (Working of Min function)
                if (self.arr[min_index]>self.arr[j]):
                    min_index=j
                    flag=1
            if flag==1:
                self.arr[i],self.arr[min_index]=self.arr[min_index],self.arr[i]
            print(f"\n\t\tARR:{self.arr}") # Uncomment If you want to see the steps
        print(f"\n\t\tAFTER SORTING,ARR:{self.arr}")


obj=SelectionSort(length=int(input("\n\t\tLENGTH:")))
obj.fill_array()
obj.Sort_arr()