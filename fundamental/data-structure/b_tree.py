"""
References:
* http://staff.ustc.edu.cn/~csli/graduate/algorithms/book6/chap19.htm
* https://gist.github.com/mateor/885eb950df7231f178a5
"""


class Node(object):

    def __init__(self):
        self.keys = []
        self.children = []
        self.leaf = True

    @property
    def size(self):
        return len(self.keys)

    def add_key(self, key):
        self.keys.append(key)
        self.keys.sort()

    def add_child(self, child):
        # Find a right place child node should be inserted.
        i = self.size - 1
        while i >= 0 and self.children[i].keys[0] > child.keys[0]:
            i -= 1
        self.children = self.children[:(i + 1)] + [child] + self.children[(i + 1):]


class BTree(object):

    def __init__(self, t):
        self.t = t  # the order of B-Tree; max size of a node
        self.root = Node()

    def search(self, key, node=None):
        if node is None:
            node = self.root

        i = 0
        while i < node.size and key > node.keys[i]:
            i += 1

        if i < node.size and key == node.keys[i]:
            return True
        if node.leaf:
            return False
        else:
            self.search(node.children[i], key)

    def insert(self, key):
        if self.__is_full(self.root):
            new_root = Node()
            new_root.children.append(self.root)
            new_root.leaf = False
            self.__split(self.root, new_root)
            self.__insert_into_nonfull(new_root, key)
        else:
            self.__insert_into_nonfull(self.root, key)

    def __split(self, full_node, parent_node):
        new_node = Node()
        new_node.leaf = full_node.leaf

        # Since node size = 2 * t - 1, t = (size + 1) / 2;
        # that is, mid = t - 1 = (size + 1) / 2 - 1 = (size - 1) / 2.
        mid = (full_node.size - 1) // 2
        parent_node.add_key(full_node.keys[mid])

        new_node.keys = full_node.keys[(mid + 1):]  # exact "mid" key goes to the parent node
        full_node.keys = full_node.keys[:mid]

        new_node.children = full_node.children[mid:]
        if len(new_node.children) > 0:
            new_node.leaf = False
        full_node.children = full_node.children[:mid]

        parent_node.add_child(new_node)

    def __insert_into_nonfull(self, nonfull_node, key):
        node = nonfull_node
        while not node.leaf:
            # Find a right child that should hold the new key.
            i = node.size - 1
            if key > node.keys[i]:
                i = node.size
            else:
                while i > 0 and key < node.keys[i]:
                    i -= 1

            child = node.children[i]
            if self.__is_full(child):
                self.__split(child, node)
                if key > node.keys[i]:
                    i += 1
                child = node.children[i]
            node = child
        node.add_key(key)

    def __is_full(self, node):
        return node.size == 2 * self.t - 1


if __name__ == '__main__':
    import random
    T = BTree(3)
    lst = [random.randint(1, 100) for i in range(10)]
    print(lst)
    for k in lst:
        T.insert(k)

    print('Inserted all values.')

    key = int(input('search key> '))
    print(T.search(key))
