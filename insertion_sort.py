"""
Insertion Sort -->  The idea of this algorithm is to build your sorted array in place, shifting elements out of the way
                    if necessary to make room as you go.
                    This algorithm has a running worst case of O(n**2), as the key moves take O(n) and the swaps and
                    comparisons also take O(n).

"""


class InsertionSort:

    def __init__(self, arr):
        self.arr = arr

    def sort_array(self):
        arr = self.arr

        for i in range(1, len(arr)):    # start with index 1 because the first element is a single element
            position = i                # position moves forward through the iteration
            key = arr[i]                # the key is the current element to be compared

            while position > 0 and arr[position-1] > key:   # keeping in the array & comparing the element to the
                                                            # left of the key
                arr[position] = arr[position-1]     # swapping the element to the left of the key with the key
                position -= 1       # decrement the position by 1 step so as to keep track of current position
            arr[position] = key     # break out of while loop and start again from next element

        return arr






