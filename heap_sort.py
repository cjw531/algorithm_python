# MinHeap from data_structure_python
class MinHeap:
    def __init__ (self):
        self.heap = []
        self.size = 0

    # O(log(n))
    def push (self, element):
        if (self.size == 0):
            self.heap.append(element)
            self.size += 1
            return
        
        self.heap.append(element)
        self.size += 1
        parent_idx = self.compute_parent(self.size - 1)
        current_idx = (self.size - 1)

        while (current_idx > 0 and self.heap[parent_idx] > element):
            # swap
            self.heap[parent_idx], self.heap[current_idx] = self.heap[current_idx], self.heap[parent_idx]
            current_idx = parent_idx
            parent_idx = self.compute_parent(current_idx)
        

    # helper function
    def compute_parent (self, child):
        parent_idx = -1
        if ((child % 2) == 1):
            parent_idx = ((child - 1) // 2)
        else: # % 2 == 0
            parent_idx = ((child - 2) // 2)

        return parent_idx

    # O(log(n))
    def pop (self):
        if (self.size == 0): 
            return
        elif (self.size == 1):
            self.heap.pop(0)
            self.size -= 1
            return
        
        # swap
        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        self.heap.pop(self.size - 1) # remove swapped root node
        self.size -= 1

        parent_idx = 0
        left_child_idx = child_idx = (2 * parent_idx) + 1
        right_child_idx = child_idx = (2 * parent_idx) + 2
        while (left_child_idx <= self.size - 1):
            if (self.heap[parent_idx] > self.heap[left_child_idx]): # left child
                self.heap[parent_idx], self.heap[left_child_idx] = self.heap[left_child_idx], self.heap[parent_idx]
        
            if (right_child_idx <= self.size - 1 and self.heap[parent_idx] > self.heap[right_child_idx]): # right child
                self.heap[parent_idx], self.heap[right_child_idx] = self.heap[right_child_idx], self.heap[parent_idx]

            parent_idx += 1
            left_child_idx = child_idx = (2 * parent_idx) + 1
            right_child_idx = child_idx = (2 * parent_idx) + 2
        
    # O(1)
    def top (self):
        return (self.heap[0])

    def is_empty (self):
        if (self.size > 0):
            return False
        return True

    def heap_size (self):
        return (self.size)

def heap_sort (array):
    result = []
    mh = MinHeap()
    for i in range (0, len(array)):
        mh.push(array[i]) # O(n log (n))
    for i in range (0, len(array)):
        result.append(mh.top()) # O(1)
        mh.pop() # O(n log (n))
    
    return result

if __name__ == '__main__':
    print ("Before sort:\t", [69,10,30,2,16,8,31,22])
    print ("After sort:\t", heap_sort([69,10,30,2,16,8,31,22]))

    print ("\nBefore sort:\t", [14,7,3,12,9,11,6,2])
    print ("After sort:\t", heap_sort([14,7,3,12,9,11,6,2]))

    print ("\nBefore sort:\t", [7, 4, 8, 2, 5, 3, 9])
    print ("After sort:\t", heap_sort([7, 4, 8, 2, 5, 3, 9]))