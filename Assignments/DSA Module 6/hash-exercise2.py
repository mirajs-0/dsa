class InventoryHashTable:
    """
    Custom hash table for product inventory.

    Rules:
    - Use a list of buckets (self.table)
    - Each bucket is a list (separate chaining)
    - Product data: sku, name, quantity
    """

    def __init__(self, size=10):
        self.size = size
        # Create a list of empty buckets (buckets are lists)
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Simple hash function for string keys.
        Example approach:
        - Sum ord(ch) for each character in key
        - Return total % self.size
        """
        return sum(ord(ch) for ch in key) % self.size

    def set_item(self, sku, name, quantity):
        """
        Add a new product or update existing one.
        - Compute bucket index with _hash
        - If sku exists in bucket -> update item
        - Else append new item to bucket
        """
        # Compute bucket index using the hash function
        index = self._hash(sku)

        # Check if the sku already exists in the bucket
        for item in self.table[index]:
            if item["sku"] == sku:
                item["name"] = name
                item["quantity"] = quantity
                return

        # If sku doesn't exist, add a new item to the bucket
        self.table[index].append({"sku": sku, "name": name, "quantity": quantity})

    def get_item(self, sku):
        """
        Return product dict if found, else None.
        - Hash sku to find bucket
        - Loop through bucket and compare item["sku"]
        """
        # Compute bucket index using the hash function
        index = self._hash(sku)

        # Loop through the bucket and look for the sku
        for item in self.table[index]:
            if item["sku"] == sku:
                return item
        return None

    def remove_item(self, sku):
        """
        Remove product by sku.
        Return True if removed, False if not found.
        - Hash sku
        - Loop through bucket with index (enumerate)
        - Delete matching item
        """
        # Compute bucket index using the hash function
        index = self._hash(sku)

        # Loop through the bucket and find the item to remove
        for i, item in enumerate(self.table[index]):
            if item["sku"] == sku:
                del self.table[index][i]
                return True
        return False

    def print_table(self):
        """
        Print all buckets and their contents.
        """
        print("\n=== Inventory Hash Table ===")
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# FOR TESTING:

inv = InventoryHashTable(size=7)

# Test adding products
inv.set_item("A101", "USB Cable", 25)
inv.set_item("B205", "Keyboard", 12)
inv.set_item("C333", "Mouse", 18)
inv.set_item("A101", "USB Cable", 30)  # update quantity

# Print the hash table
inv.print_table()

# Test searching for products
print("Search B205:", inv.get_item("B205"))

# Test removing a product
print("Remove C333:", inv.remove_item("C333"))

# Print the updated hash table
inv.print_table()