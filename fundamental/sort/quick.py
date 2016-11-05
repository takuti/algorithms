""" QUICKSORT
"""

import random


class Q:

    def __init__(self, size=100):
        self.size = size
        self.q = [0] * size
        self.head = 0
        self.tail = 0

    def is_non_empty(self):
        return self.head != self.tail

    def enqueue(self, e):
        self.q[self.tail] = e
        self.tail += 1
        if self.tail == self.size:
            self.tail = 0

    def dequeue(self):
        res = self.q[self.head]
        self.head += 1
        if self.head == self.size:
            self.head = 0
        return res


def partition(A, p, r):
    # all left elements should be less than or equal to `pivot`
    # all right elements should be greater than `pivot`
    pivot = A[p]

    k = p + 1
    l = r

    # A[k] should be left-most element which greater than pivot
    while (A[k] <= pivot) and (k < r):
        k += 1

    # A[l] should be right-most element which less than or equal to pivot
    while (A[l] > pivot):
        l -= 1

    while (k < l):
        # swap left-most `> pivot` element and right-most `<= pivot` element
        A[k], A[l] = A[l], A[k]

        # find left-most again
        while (A[k] <= pivot):
            k += 1

        # find right-most again
        while (A[l] > pivot):
            l -= 1

    # last `<= pivot` element is swapped with pivot
    A[p], A[l] = A[l], A[p]

    return l


def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)


def sort(A, p, r, randomize_flg=False):
    """
    >>> sort([43, 2, 15, 81, 49, 4, 56, 11, 51, 97], 0, 9)
    [2, 4, 11, 15, 43, 49, 51, 56, 81, 97]
    >>> sort([43, 2, 15, 81, 49, 4, 56, 11, 51, 97], 0, 9, True)
    [2, 4, 11, 15, 43, 49, 51, 56, 81, 97]
    """
    if p < r:
        q = randomized_partition(A, p, r) if randomize_flg else partition(A, p, r)
        sort(A, p, q - 1)
        sort(A, q + 1, r)
    return A


def sort_iter(A, p, r, randomize_flg=False):
    """
    >>> sort([43, 2, 15, 81, 49, 4, 56, 11, 51, 97], 0, 9)
    [2, 4, 11, 15, 43, 49, 51, 56, 81, 97]
    >>> sort([43, 2, 15, 81, 49, 4, 56, 11, 51, 97], 0, 9, True)
    [2, 4, 11, 15, 43, 49, 51, 56, 81, 97]
    """
    queue = Q()
    queue.enqueue((p, r))

    while queue.is_non_empty():
        p, r = queue.dequeue()
        if p < r:
            q = randomized_partition(A, p, r) if randomize_flg else partition(A, p, r)
            queue.enqueue((p, q - 1))
            queue.enqueue((q + 1, r))

    return A


if __name__ == '__main__':
    import doctest
    doctest.testmod()
