# This File Contains about How to do Merge Sort in Python
# APart from Bubble,Insertion,selection sort, Merge sort is very less runtime taker because it applies divide and conquer algorithm
# Here as a mutable array we will take list DS

'''
Rules:
1) Search Mid value by applying Divide and conquer algo
2) From Mid , divide the total array into Two subarrays :Left and Right
3) Find mid from both arrays and break them
4) After sorting, choose each elemnts from both subarrays , compare them , and put them in a 3rd array in correct order
'''

class RecMergeSort:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
    
    def merge(self, left: list[int], right: list[int]) -> list[int]:
        merged = []
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged



print(RecMergeSort().sortArray([-11, 100, 0, 5, -5, 9]))