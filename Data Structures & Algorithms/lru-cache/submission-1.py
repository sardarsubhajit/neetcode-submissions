class DoublyListNode:
    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = dict()

        self.left, self.right = DoublyListNode(), DoublyListNode()
        self.left.next, self.right.prev = self.right, self.left        

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
    
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        node.prev, node.next = prv, nxt
        prv.next = nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.remove(self.cache[key])
        self.cache[key] = DoublyListNode(key=key, val=value)
        self.insert(self.cache[key])

        if len(self.cache) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]