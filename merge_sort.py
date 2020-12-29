def merge_sort (array):
    if (len(array) <= 1):
        return array

    # divide
    middle = len(array) // 2
    
    # recursive call
    left = merge_sort(array[:middle]) 
    right = merge_sort(array[middle:])

    # conquer
    return merge(left, right)

def merge (left, right):
    result = []

    # as long as both list have elements left
    while (len(left) > 0 and len(right) > 0):
        # compare 1st elements in each list, then append
        if (left[0] <= right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # if elements remaining in left
    while (len(left) > 0):
        result.append(left.pop(0))

    # if elements remaining in right
    while (len(right) > 0):
        result.append(right.pop(0))

    return result

if __name__ == '__main__':
    print ("Before merge:\t", [69,10,30,2,16,8,31,22])
    print ("After merge:\t", merge_sort([69,10,30,2,16,8,31,22]))

    print ("\nBefore merge:\t", [14,7,3,12,9,11,6,2])
    print ("After merge:\t", merge_sort([14,7,3,12,9,11,6,2]))
