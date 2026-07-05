from collections import defaultdict

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add(self, node):
        """Add node right after head (Most Recently Used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        """Remove an existing node."""
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        """Remove Least Recently Used node."""
        if self.size == 0:
            return None

        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0

        # key -> node
        self.nodes = {}

        # freq -> DLL
        self.freqMap = defaultdict(DoublyLinkedList)

    def updateFreq(self, node):
        freq = node.freq

        # Remove from current frequency list
        self.freqMap[freq].remove(node)

        # Update minimum frequency if needed
        if freq == self.minFreq and self.freqMap[freq].size == 0:
            self.minFreq += 1

        # Increase frequency
        node.freq += 1

        # Add to new frequency list
        self.freqMap[node.freq].add(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.updateFreq(node)
        return node.value

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self.updateFreq(node)
            return

        if len(self.nodes) == self.capacity:
            # Remove LFU node
            lfu = self.freqMap[self.minFreq].remove_last()
            del self.nodes[lfu.key]

        # Insert new node
        node = Node(key, value)
        self.nodes[key] = node
        self.freqMap[1].add(node)
        self.minFreq = 1