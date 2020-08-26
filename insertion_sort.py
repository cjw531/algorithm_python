# O(n^2)
def insertion_sort (array):
    result = [array[0]]
    array.pop(0)
    flag = False
    while (len(array) > 0):
        flag = False
        for i in range (0, len(result)):
            if (result[i] > array[0]):
                result.insert(i, array[0])
                array.pop(0)
                flag = True
                break
        if (not flag):
            result.append(array[0])
            array.pop(0)
    
    return result

if __name__ == '__main__':
    print ("Original array:\t\t", [64, 25, 12, 22, 11])
    print ("After selection sort:\t", insertion_sort([64, 25, 12, 22, 11]))
    print ("Original array:\t\t", [7, 4, 8, 2, 5, 3, 9])
    print ("After selection sort:\t", insertion_sort([7, 4, 8, 2, 5, 3, 9]))