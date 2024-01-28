import random

def bubblesort(elements):
    
    for i in range(len(elements)):
        for j in range(0, len(elements)-i-1):
            if elements[j] > elements[j+1]:
                # Swap if the element found is greater than the next element
                elements[j], elements[j+1] = elements[j+1], elements[j]


elements = [random.randint(1, 50) for _ in range(50)]
 
print("Unsorted list is,")
print(elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)
