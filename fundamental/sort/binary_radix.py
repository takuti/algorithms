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


def bits(n, b_pos, m):
    b = format(n, 'b')

    if len(b) < (b_pos + m):
        b = b.zfill(b_pos + m)

    return b[::-1][b_pos:(b_pos + m)]


def partition(A, p, r, b_pos):
    k = p
    l = r

    # A[k] should be left-most element b_pos-th element is 1
    while (k < r) and (bits(A[k], b_pos, 1) == '0'):
        k += 1

    # A[l] should be right-most element b_pos-th element is 0
    while (l > p) and (bits(A[l], b_pos, 1) == '1'):
        l -= 1

    while (k < l):
        A[k], A[l] = A[l], A[k]

        # find left-most again
        while (bits(A[k], b_pos, 1) == '0'):
            k += 1

        # find right-most again
        while (bits(A[l], b_pos, 1) == '1'):
            l -= 1

    return l


def sort_exchange(A, p, r, b_pos):
    """
    >>> sort_exchange([43, 2, 15, 81, 49, 4, 56, 11, 51, 97], 0, 9, 32)
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


def sort_straight(A, N, b):
    """
    >>> sort_straight([43, 2, 15, 81, 49, 4, 56, 11, 51, 97], 10, 32)
    [2, 4, 11, 15, 43, 49, 51, 56, 81, 97]
    """

    # this should be small enough depending on minimum element
    mbits = 1

    # `mbits` bits per pass = 2^mbits possible patterns
    M = 2 ** mbits

    n_pass = int(b / mbits)
    for ps in range(n_pass):
        # count `ps`-th `mbits` bits of each element
        # (index corresponds to its decimal repr.)
        count = [0] * M
        for i in range(N):
            d_ps = int(bits(A[i], ps * mbits, mbits), 2)
            count[d_ps] += 1

        # Counting Sort:
        # prefix sum on counts
        # each element indicates the last index of sequence of `mbits` bits
        count[0] -= 1  # decrement because index starts from 0
        for j in range(1, M):
            count[j] += count[j - 1]

        # copy elements in A to tA
        tA = [0] * N
        for i in range(N - 1, -1, -1):
            d_ps = int(bits(A[i], ps * mbits, mbits), 2)
            tA[count[d_ps]] = A[i]
            count[d_ps] -= 1
        A, tA = tA, A

    return A


def sort_straight_2(A, N, b):
    """
    >>> sort_straight_2([43, 2, 15, 81, 49, 4, 56, 11, 51, 97], 10, 32)
    [2, 4, 11, 15, 43, 49, 51, 56, 81, 97]
    """

    # this should be small enough depending on minimum element
    mbits = 1

    # `mbits` bits per pass = 2^mbits possible patterns
    M = 2 ** mbits

    tA = [0] * N
    n_pass = int(b / mbits)

    for ps in range(n_pass):
        bitsA = [int(bits(a, ps * mbits, mbits), 2) for a in A]

        # (Strictly Iterative) Counting Sort
        offset = -1
        for j in range(M):
            count = 0

            for i in range(N):
                if bitsA[i] == j:
                    count += 1

            rank = offset + count

            for i in range(N - 1, -1, -1):
                if bitsA[i] == j:
                    tA[rank] = A[i]
                    rank -= 1

            offset += count
        A, tA = tA, A

    return A


if __name__ == '__main__':
    import doctest
    doctest.testmod()
