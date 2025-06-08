class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize an empty table with lists for chaining.

    def _hash(self, key):
        """Compute the hash index for a given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        # Check if the key already exists and update the value if it does.
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If the key does not exist, append it to the list at the index.
        self.table[index].append([key, value])

    def get(self, key):
        """Retrieve a value by its key."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        # If the key is not found, raise an exception.
        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        """Remove a key-value pair from the hash table."""
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        # If the key is not found, raise an exception.
        raise KeyError(f"Key '{key}' not found")

    def display(self):
        """Display the contents of the hash table."""
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

# Example usage
hash_table = HashTable()

# Insert some key-value pairs
hash_table.insert("a", 1)
hash_table.insert("b", 2)
hash_table.insert("c", 3)

# Retrieve values
print("Value for key 'a':", hash_table.get("a"))  # Output: 1

# Delete a key
hash_table.delete("b")

# Display the hash table
hash_table.display()


