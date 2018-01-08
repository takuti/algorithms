"""Binary-search-tree
"""


class Node(object):

    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


class Tree(object):

    def __init__(self):
        self.root = None

    def walk(self, x):
        if x is not None:
            self.walk(x.left)
            print(x.key)
            self.walk(x.right)

    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            x = x.left if z.key < x.key else x.right
        z.parent = y
        if y is None:
            self.root = z  # z is the first node
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def search(self, x, k):
        while x is not None and x.key is not k:
            x = x.left if k < x.key else x.right
        return x

    def minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def maximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def successor(self, x):
        """Return node which will be printed next to x in walk()
        """
        if x.right is not None:
            return self.minimum(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def transplant(self, u, v):
        """Replace root from u to v
        """
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y


if __name__ == '__main__':
    import random
    T = Tree()
    lst = [random.randint(1, 100) for i in range(10)]
    print(lst)
    for k in lst:
        T.insert(Node(k))
    T.walk(T.root)

    print('---')

    x = T.successor(T.search(T.root, lst[5]))
    if x is None:
        print('%d is the last.' % lst[5])
    else:
        print('next to %d is %d' % (lst[5], x.key))

    print('---')

    for k in lst:
        T.delete(T.search(T.root, k))
    T.walk(T.root)
