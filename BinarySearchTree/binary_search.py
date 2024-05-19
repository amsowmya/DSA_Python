def linear_search(numbers_list, num_to_find):
    for index, element in enumerate(numbers_list):
        if element == num_to_find:
            return index
    return -1 

def binary_search(numbers_list, num_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]
        
        if mid_number == num_to_find:
            return mid_index
        
        if mid_number < num_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index -1 
            
    return -1

def binary_search_recursion(numbers_list, num_to_find, left_index, right_index):
    if left_index > right_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    
    if mid_index < 0 or mid_index >= len(numbers_list):
        return -1
    
    mid_number = numbers_list[mid_index]
    
    if mid_number == num_to_find:
        return mid_index
    
    if mid_number < num_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index -1
        
    return binary_search_recursion(numbers_list, num_to_find, left_index, right_index)
    
    
    
lists = [4,6,8,9,10,121]

linear_result = linear_search(lists, 10)
print("Linear search : ", linear_result)

binary_result = binary_search(lists, 10)
print("Binary search : ", binary_result)

recursion_result = binary_search_recursion(lists, 10, 0, len(lists)-1)
print("Binary search resursion : ", recursion_result)