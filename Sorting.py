#!/usr/bin/env python
# coding: utf-8

# In[6]:


class ArraySort():
    
    def __init__(self,input_array):
        self.input_array = input_array 

    # Insertion sort function 
    def insertionSort(self):
        
        # Traverse through 1 to len(arr)
        for i in range(1, len(self.input_array)):  
            
            key = self.input_array[i]
            
            
            j = i-1
            while j >= 0 and key < self.input_array[j] :
                    self.input_array[j + 1] = self.input_array[j]
                    j -= 1
            self.input_array[j + 1] = key
            
        return self.input_array 
    
    # Merge sort function
    def mergeSort_help(self,array):
        
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]

            # Recursive call on each half
            self.mergeSort_help(left)
            self.mergeSort_help(right)

            # Two iterators for traversing the two halves
            i = 0
            j = 0
        
            # Iterator for the main list
            k = 0
        
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                  # The value from the left half has been used
                  array[k] = left[i]
                  # Move the iterator forward
                  i += 1
                else:
                    array[k] = right[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k]=right[j]
                j += 1
                k += 1

    
    def mergeSort(self):
        self.mergeSort_help(self.input_array)
        return self.input_array

    def __main__(self, sort_method):
        if sort_method == 'insertion_sort':
            return self.insertionSort() 
        elif sort_method == 'merge_sort':
            return self.mergeSort() 
        else:
            return "sort method parameter error" 


arr = [534,215,353,3,58,-3,4,-23,79,0,2]
sortclass = ArraySort(arr)

print("Choose the sort method: \n 1. Insertion Sort \n 2. Merge Sort")
x=input("")
if (x=="Insertion Sort"):
    output=sortclass.mergeSort()
    print(output) 
else:
    output2 = sortclass.__main__(sort_method='insertion_sort') 
    print(output2)


# In[ ]:




