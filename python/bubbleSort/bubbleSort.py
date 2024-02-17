import random

def bubble_sort(array):
    array_length = len(array)
    
    for pass_number in range(array_length):
        for index in range(0, array_length - pass_number - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]


array = [random.randint(1, 75) for _ in range(50)]
 
print("Unsorted list is,")
print(array)
bubble_sort(array)
print("Sorted Array is, ")
print(array)
