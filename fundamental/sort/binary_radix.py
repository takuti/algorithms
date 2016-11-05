"""Radix sort for binary representations
"""


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


def bit(v, n, b_pos):
    return format(v, 'b').zfill(n)[b_pos]


def partition(A, p, r, b_pos, n=10):
    k = p
    l = r

    b_pos = n - b_pos

    # A[k] should be left-most element b_pos-th element is 1
    while (k < r) and (bit(A[k], n, b_pos) == '0'):
        k += 1

    # A[l] should be right-most element b_pos-th element is 0
    while (l > p) and (bit(A[l], n, b_pos) == '1'):
        l -= 1

    while (k < l):
        A[k], A[l] = A[l], A[k]

        # find left-most again
        while (bit(A[k], n, b_pos) == '0'):
            k += 1

        # find right-most again
        while (bit(A[l], n, b_pos) == '1'):
            l -= 1

    return l


def sort_exchange(A, p, r, b_pos):
    """
    >>> sort_exchange([43, 2, 15, 81, 49, 4, 56, 11, 51, 97], 0, 9, 10)
    [2, 4, 11, 15, 43, 49, 51, 56, 81, 97]
    """
    queue = Q()
    queue.enqueue((p, r, b_pos))

    while queue.is_non_empty():
        p, r, b_pos = queue.dequeue()
        b_pos -= 1

        if (p < r) and (b_pos >= 0):
            q = partition(A, p, r, b_pos)
            queue.enqueue((p, q, b_pos))
            queue.enqueue((q + 1, r, b_pos))

    return A


if __name__ == '__main__':
    import doctest
    doctest.testmod()
