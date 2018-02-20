"""
MergeSort --> Divide & Conquer --> This algorithm has two big ideas, the first is to continually divide the problem
              until a size of one is achieved, this is done recursively. The second big idea is the merging and sorting
              of each of the singular elements, sorting as we merge until finally we are left with a sorted array of
              size n.

"""


def divide(arr):
    """
    Recursive function that calls itself until the input is an array of size 1

    :param arr: unsorted array of size n
    :return: calls the merge function when the array dept is (1+log n) and we have n number of leaves
    """
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = divide(arr[:middle])
    right = divide(arr[middle:])

    return merge(left, right)


def merge(left, right):
    i, j = 0, 0  # i (left array index), j (right array index)
    sorted_arr = []  # initialized empty array to which we can append elements in order of size

    while i < len(left) and j < len(right):  # ensure we don't over shoot the arrays
        if left[i] < right[j]:  # conditionally sort the elements based on size and add to the empty list
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    if i == len(left) or j == len(right):           # which ever array we sort through first i.e left or right
        sorted_arr.extend(left[i:] or right[j:])    # join the left overs from the other to the end as they will by
                                                    # default be larger and already sorted
    return sorted_arr


if __name__ == '__main__':
    test = [4, 2, 3, 8, 8, 43, 6, 1, 0]
    test_case = divide(test)
    print(test, len(test), test_case, len(test_case))
