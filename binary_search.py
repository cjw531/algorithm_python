def binary_search (sorted_list, begin, end, key):
    if (begin > end):
        print ("ERROR: Index Out of Bound") 
        return None
    
    middle_index = (begin + end) // 2
    middle_elem = sorted_list[middle_index]
    if (key < middle_elem):
        return binary_search(sorted_list, begin, middle_index - 1, key)
    elif (key > middle_elem):
        return binary_search(sorted_list, middle_index + 1, end, key)
    else:
        return middle_index

if __name__ == '__main__':
    print ("Index of 15:", binary_search([1,3,8,11,15,17,20], 0, 6, 15))
    print ("Index of 1:", binary_search([1,3,8,11,15,17,20], 0, 6, 1))
    print ("Index of 20:", binary_search([1,3,8,11,15,17,20], 0, 6, 20))
    print ("Index of 11:", binary_search([1,3,8,11,15,17,20], 0, 6, 11))
