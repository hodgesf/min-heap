# Name: Frank Hodges
# OSU Email: hodgesf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5 - Heap structures and methods
# Due Date: 11/30
# Description: MinHeap implementation using the dynamic array file previous written in other assignments.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        This method adds a new object to the MinHeap while maintaining heap property.
        The runtime complexity of this implementation is O(log N).
        """
        self._heap.append(node)
        index = self._heap.length() - 1
        while index > 0:
            parent_index = (index - 1) // 2  # Calculate the parent index
            if self._heap[index] < self._heap[parent_index]:  # Compare priorities
                # Swap the node with its parent
                self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
                index = parent_index  # Update the index to the parent's index
            else:
                break  # If the condition is not met, break out of the loop


    def is_empty(self) -> bool:
        """
        This method returns True if the heap is empty; otherwise, it returns False.
        The runtime complexity of this implementation is O(1).
        """
        return self._heap.is_empty()


    def get_min(self) -> object:
        """
        This method returns an object with the minimum key, without removing it from the heap. If
        the heap is empty, the method raises a MinHeapException.
        The runtime complexity of this implementation is O(1).
        """
        if self._heap.is_empty():
            raise MinHeapException()
        return self._heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        This method returns an object with the minimum key, and removes it from the heap. If the
        heap is empty, the method raises a MinHeapException.
        For the downward percolation of the replacement node: if both children of the node have
        the same value (and are both smaller than the node), swap with the left child.
        The runtime complexity of this implementation is O(log N).
        """
        if self._heap.is_empty():
            raise MinHeapException("Heap is empty")

        # Get the minimum value (at index 0)
        min_value = self._heap.get_at_index(0)

        # Replace the root node with the last node in the heap
        size_heap = self._heap.length()
        last_node = self._heap.get_at_index(size_heap - 1)
        self._heap.set_at_index(0, last_node)

        # Remove the last node from the heap
        self._heap.remove_at_index(size_heap - 1)

        # Perform downward percolation to maintain the heap property
        _percolate_down(self._heap, size_heap - 1, 0)

        return min_value

    def build_heap(self, da: DynamicArray) -> None:
        """
        This method receives a DynamicArray with objects in any order, and builds a proper
        MinHeap from them. The current content of the MinHeap is overwritten.
        The runtime complexity of this implementation is O(N).
        """
        self._heap = DynamicArray(da)  # Create a new DynamicArray instance with the content from da
        index = (self._heap.length() // 2) - 1  # Start from the last non-leaf node

        # Perform heapify operation from the last non-leaf node up to the root
        while index >= 0:
            _percolate_down(self._heap, self._heap.length(), index)
            index -= 1

    def size(self) -> int:
        """
        This method returns the number of items currently stored in the heap.
        The runtime complexity of this implementation is O(1).
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        This method clears the contents of the heap.
        The runtime complexity of this implementation is O(1)
        """
        self._heap = DynamicArray()  # Create an empty DynamicArray


def _percolate_down(arr, size, index):
    """
    Helper function to percolate down the heap maintaining the min-heap property.
    """
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    # Find the smallest among the node and its children
    if left < size and arr[left] < arr[smallest]:
        smallest = left

    if right < size and arr[right] < arr[smallest]:
        smallest = right

    # If the smallest node is not the current node, swap them and percolate down
    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        _percolate_down(arr, size, smallest)



def heapsort(da: DynamicArray) -> None:
    """
    receives a DynamicArray and sorts its content in non-ascending order,
    using the Heapsort algorithm. array is sorted in place. This function does not return anything.
    You may assume that the input array will contain one or more homogeneous elements
    (either all numbers, or strings, or custom objects, but never a mix of these). You do not
    need to write checks for these conditions.
    The runtime complexity of this implementation is O(N log N).
    """
    # Build a max heap from the given DynamicArray
    size = da.length()
    # Start from the last non-leaf node
    for i in range(size // 2 - 1, -1, -1):
        _percolate_down(da, size, i)

    # Extract elements one by one from the heap and place them at the end
    for i in range(size - 1, 0, -1):
        da[i], da[0] = da[0], da[i]  # Swap the root (max element) with the last element
        _percolate_down(da, i, 0)  # Heapify the reduced heap

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
