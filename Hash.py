class ListNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

class HashTable:
    def __init__(self, initial_capacity=16):
        self.capacity = initial_capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash(self, key):
        A = 0.6180339887
        return int(self.capacity * (key * A - int(key * A)))

    def resize(self, new_capacity):
        new_table = [None] * new_capacity
        for bucket in self.table:
            current = bucket
            while current:
                index = self.hash(current.key) % new_capacity
                next_node = current.next
                if not new_table[index]:
                    new_table[index] = current
                    current.prev = None
                    current.next = None
                else:
                    current.next = new_table[index]
                    new_table[index].prev = current
                    new_table[index] = current
                current = next_node
        self.table = new_table
        self.capacity = new_capacity

    def insert(self, key, data):
        index = self.hash(key) % self.capacity
        new_node = ListNode(key, data)
        if not self.table[index]:
            self.table[index] = new_node
        else:
            new_node.next = self.table[index]
            self.table[index].prev = new_node
            self.table[index] = new_node
        self.size += 1
        if self.size >= self.capacity * 3 / 4:
            self.resize(self.capacity * 2)

    def search(self, key):
        index = self.hash(key) % self.capacity
        current = self.table[index]
        while current:
            if current.key == key:
                return current.data
            current = current.next
        return None

    def remove(self, key):
        index = self.hash(key) % self.capacity
        current = self.table[index]
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.table[index] = current.next
                if current.next:
                    current.next.prev = current.prev
                self.size -= 1
                if self.size <= self.capacity / 4 and self.capacity > 16:
                    self.resize(self.capacity // 2)
                return True
            current = current.next
        return False

# Example usage
hash_table = HashTable()

# Insert some values
hash_table.insert(1, 10)
hash_table.insert(2, 20)
hash_table.insert(3, 30)

# Search for a value
result = hash_table.search(2)
if result is not None:
    print("Value found:", result)
else:
    print("Value not found.")

# Remove a value
if hash_table.remove(2):
    print("Value removed successfully.")
else:
    print("Value not found.")
