"""Inspired by http://www.maxburstein.com/blog/creating-a-simple-bloom-filter/"""

from bitarray import bitarray
import mmh3


class BloomFilter(object):

    def __init__(self, size, num_hashes):
        """
        >>> b = BloomFilter(500000, 7)
        >>> b.add('test')
        >>> 'test' in b
        True
        >>> 'foo' in b
        False
        """
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, key):
        for seed in range(self.num_hashes):
            h = mmh3.hash(key, seed) % self.size
            self.bit_array[h] = 1

    def __contains__(self, key):
        for seed in range(self.num_hashes):
            h = mmh3.hash(key, seed) % self.size
            if self.bit_array[h] == 0:
                return False
        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
