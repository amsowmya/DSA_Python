
# Time complexity for Bubble sort is : 0(n2)

def bubble_sort(elements):
    size = len(elements)
    
    for i in range(size-1):
        swapped = False
        for j in range(size-1):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped=True
        if not swapped:
            break
    return elements
        
        
print(bubble_sort([5,3,6,1,0,-9]))