"""
Problem Set Dynamic connectivity.

The input is a sequence of pairs of integers, where each integer represents an object of some type and we are to
interpret the pair p q as meaning p is connected to q. We assume that "is connected to" is an equivalence relation:

    symmetric: If p is connected to q, then q is connected to p.
    transitive: If p is connected to q and q is connected to r, then p is connected to r.
    reflexive: p is connected to p.

An equivalence relation partitions the objects into equivalence classes or connected components.

Our goal is to write a program that given a set number N, will initialize a data representation that we can then perform
the two operations:

    join p to q - Union Operation
    check if p is connected to q - is_connected Operation
"""

"""
Method No.1-->  Eager Approach --> Quadratic --> takes N^2 array accesses to process a sequence of union commands 
                on N objects. 
                O(N**2) - Slow
"""


class UnionFindEager:

    def __init__(self, n):
        """ initialize an empty UnionFind object with N number of items """
        self.parent_arr = list(range(n))
        self._id = list(range(n))
        self._count = n

    def union(self, p, q):
        """ joins p and q together by changing the _id of p and its
            connected components to the _id of q """
        _id = self._id
        id_p = _id[p]
        id_q = _id[q]
        for (i, item) in enumerate(_id):
            if item == id_p:
                _id[i] = id_q
            continue
        return _id

    def is_connected(self, p, q):
        """ checks if the id[p] --> matches --> id[q] and returns answer """
        _id = self._id
        id_p = _id[p]
        id_q = _id[q]
        if id_p == id_q:
            return f'{p} and {q} are connected'
        else:
            return f'{p} and {q} are not connected'


"""
Method No.2--> Lazy Approach --> small improvement but worst case could be too expensive to implement. Could end up
               with one long tree meaning the find method could take N array accesses.  
               O(N) - Still too slow - Avoid
"""


class UnionFindLazy:

    def __init__(self, n):
        """ initialize an empty UnionFind object with N number of items """
        self.parent_arr = list(range(n))
        self._id = list(range(n))
        self._count = n

    def root(self, i):
        """ follows the parent pointers until the root is found """
        _id = self._id
        while i != _id[i]:
            i = _id[i]
        return i

    def union(self, p, q):
        """ joins p and q together by changing the root of p and its
                    connected components to the root of q """
        _id = self._id
        _p, _q = self.root(p), self.root(q)  # Get the root of p & q
        _id[_p] = _q  # join the root of p to the root of q
        return self.parent_arr, _id  # return tuple of the data structures for debugging and visualization

    def is_connected(self, p, q):
        """ checks if p and q have the same root """
        if self.root(p) == self.root(q):
            return f'{p} and {q} are connected'
        else:
            return f'{p} and {q} are not connected'


"""
Method No.3--> Weighted --> Improving upon the lazy approach by ensuring the trees never get too big. Extra array called
                            num_obj created to keep track of how many objects are rooted at tree i. Only the root and 
                            union method is modified, all other methods are inherited from the parent UnionFindLazy.
                            with out path compression the algorithm is lg N (base-2). However, by adding path 
                            compression and keeping the trees relatively flat it, any sequence of M union-find 
                            operations on N objects makes >= (N + M lg* N) array accesses. This algorithm in practices 
                            behaves in a linear fashion.    git config --global user.email "you@example.com"
                            O(N + M lg* N) - wicked fast                             
"""


class UnionFindWeighted(UnionFindLazy):

    def __init__(self, n):
        self.num_obj = [1] * n
        super().__init__(n)

    def root_compression(self, i):
        _id = self._id
        while i != _id[i]:
            _id[i] = _id[_id[i]]    # path compression (halving the path length)
            i = _id[i]
        return i

    def union(self, p, q):
        """ Over ride of the union method """
        parent_arr = self.parent_arr
        num_obj = self.num_obj
        _id = self._id
        _p = self.root_compression(p)
        _q = self.root_compression(q)

        if _p == _q:
            return f'{p} and {q} are already joined.'  # if the roots of p & q are the same they are already connected
        elif num_obj[_p] < num_obj[_q]:  # determine which tree is bigger and link the root of the smaller to
            _id[_p] = _q  # the root of the larger.
            num_obj[_q] += num_obj[_p]
        else:
            _id[_q] = _p
            num_obj[_p] += num_obj[_q]
        return parent_arr, _id, num_obj  # return tuple of the data structures for debugging and visualization
