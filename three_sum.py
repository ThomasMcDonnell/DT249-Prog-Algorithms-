"""
Problem set 3-Sum.

Given N distinct integers, how many triples sum to exactly zero?

Application: --> Important for problems in computational geometry

Example: --> [30, -40, -20, -10, 40, 0, 10, 5]

"""

"""
Method No.1--> Brute force approach runs in O(n^3) time as we have three nested loops. Not a very efficient as the size 
of n (integers) increases.  
"""


class BruteForceSearch:

    def __init__(self, arr):
        self.arr = arr

    def three_sum_brute_force(self):
        """
        Three nested loops, checks the sum of three elements in a list against the given condition 0. If the three add to 0
        then the count is incremented by 1 and the third loop k moves to the next element .... Once all possible combinations
        of i and j have been checked against n elements in the list j moves on to the next element and the process is
        repeated until such point that i moves on to the next element and the above steps are repeated.
        :param a: list of integers
        :return: count --> number of times the sum of three amount to zero.
        """
        a = self.arr
        n = len(a)
        count = 0

        for i in range(0, n):  # first iteration
            for j in range(i + 1, n):  # second iteration (i+1) insures we don't use the same element more than once
                for k in range(j + 1, n):  # third iteration (j+1) insures we don't use the same element more than once
                    if a[i] + a[j] + a[k] == 0:  # if the sum of 3 == 0
                        count += 1  # the count is incremented by one and moves on -->
        return count


"""
Method No.2 --> Binary Search Method --> first the array given is sorted, than if one number is fixed the question can 
                changed to ; find the sum of two numbers that when added to the first amount to a target number (0).
                Much more efficient than the brute force attempt and takes roughly O(n^2) time.    
"""


class SortedSearch:

    def __init__(self, arr):
        self.sorted_arr = sorted(arr)

    def three_sum(self, target):
        arr = self.sorted_arr   # sort the array
        n = len(arr)            # n represents the length of the given arr
        triplets = set()        # to be sure we do not have any duplicates we save the results to a set

        for i, num in enumerate(arr):
            if i > n - 3:
                break

            j, k = i + 1, n - 1

            while j < k:
                _sum = num + arr[j] + arr[k]    # see if the sum of elements == target
                if _sum == target:
                    triplet = [num, arr[j], arr[k]]            # if sum of three numbers == target
                    triplets.add(tuple(triplet))               # add numbers to a set, which ensures unique triplets
                    k -= 1                      # move k back 1
                    j += 1                      # move j forward 1
                elif _sum > target:
                    k -= 1
                else:
                    j += 1
        return len(triplets)
