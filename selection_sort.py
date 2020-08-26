"""
selection sort is good for small size array
for small size array, it is faster than merge sort
runtime: O(n^2)
"""
def selection_sort (array):
    result = []
    while (len(array) > 0):
        min = array[0]
        idx = 0
        for i in range (0, len(array)):
            if (min > array[i]):
                min = array[i]
                idx = i
        result.append(min)
        array.pop(idx)
    
    return result

if __name__ == '__main__':
    print ("Original array:\t\t", [64, 25, 12, 22, 11])
    print ("After selection sort:\t", selection_sort([64, 25, 12, 22, 11]))
    print ("Original array:\t\t", [7, 4, 8, 2, 5, 3, 9])
    print ("After selection sort:\t", selection_sort([7, 4, 8, 2, 5, 3, 9]))