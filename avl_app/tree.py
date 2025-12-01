"""AVL Tree implementation with self-balancing for course schedule storage."""


class AVLNode:
    """A node in the AVL Tree with height tracking."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    """Self-balancing AVL Tree with insert, search, traversal, and height operations."""
    
    def __init__(self):
        """Initialize an empty AVL tree."""
        self.root = None

    def _node_height(self, node) -> int:
        """Get height of a node (0 if None)."""
        return node.height if node else 0

    def _balance_factor(self, node) -> int:
        """Calculate balance factor: left height - right height."""
        return self._node_height(node.left) - self._node_height(node.right) if node else 0

    def _update_height(self, node):
        """Update node's height based on children."""
        node.height = 1 + max(self._node_height(node.left), self._node_height(node.right))

    def _rotate_right(self, y):
        """Perform right rotation on node y."""
        x = y.left
        t2 = x.right
        x.right = y
        y.left = t2
        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x):
        """Perform left rotation on node x."""
        y = x.right
        t2 = y.left
        y.left = x
        x.right = t2
        self._update_height(x)
        self._update_height(y)
        return y

    def insert(self, key, value):
        """Insert a key-value pair and rebalance if needed."""
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        """Recursive insert with AVL rebalancing."""
        if not node:
            return AVLNode(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            return node

        self._update_height(node)
        balance = self._balance_factor(node)

        # Left-Left case
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        # Right-Right case
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        # Left-Right case
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        # Right-Left case
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

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
        return self._node_height(self.root)

    def find_by_prefix(self, prefix: tuple) -> list:
        """Find all items whose key starts with the given prefix tuple."""
        result = []
        prefix_len = len(prefix)
        for item in self.inorder():
            if item.get_key()[:prefix_len] == prefix:
                result.append(item)
        return result
