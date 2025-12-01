"""Binary Search Tree implementation for course schedule storage."""


class BSTNode:
    """A node in the Binary Search Tree."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    """Binary Search Tree with insert, search, traversal, and height operations."""
    
    def __init__(self):
        """Initialize an empty BST."""
        self.root = None

    def insert(self, key, value):
        """Insert a key-value pair into the tree."""
        if self.root is None:
            self.root = BSTNode(key, value)
        else:
            self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        """Recursive helper for insert."""
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key, value)
            else:
                self._insert(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key, value)
            else:
                self._insert(node.right, key, value)

    def search(self, key):
        """Search for a value by key. Returns None if not found."""
        return self._search(self.root, key)

    def _search(self, node, key):
        """Recursive helper for search."""
        if node is None or node.key == key:
            return node.value if node else None
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder(self) -> list:
        """Return all values in sorted order via in-order traversal."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        """Recursive helper for in-order traversal."""
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def height(self) -> int:
        """Return the height of the tree. Empty tree has height 0."""
        return self._height(self.root)

    def _height(self, node) -> int:
        """Recursive helper to compute height of a subtree."""
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def find_by_prefix(self, prefix: tuple) -> list:
        """Find all items whose key starts with the given prefix tuple."""
        result = []
        prefix_len = len(prefix)
        for item in self.inorder():
            if item.get_key()[:prefix_len] == prefix:
                result.append(item)
        return result
