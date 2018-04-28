########################################
# PROJECT XXX - Max Heap and Sort
# Author:
# PID:
########################################
# import hashlib
#
# class Node:
#     # DO NOT MODIFY THIS CLASS #
#     __slots__ = 'key', 'value', 'next_node'
#
#     def __init__(self, value, parent=None, left=None, right=None):
#         """
#         Initialization of a node
#         :param value: value stored at the node
#         :param parent: the parent node
#         :param left: the left child node
#         :param right: the right child node
#         """
#         self.value = value
#         self.parent = parent
#         self.left = left
#         self.right = right
#
#     def __eq__(self, other):
#         """
#         DO NOT EDIT
#         Determine if two nodes are equal (same value)
#         :param other: node to compare to
#         :return: True if nodes are equal, False otherwise
#         """
#         if other is None:
#             return False
#         if self.value == other.value and self.key == other.key:
#             return True
#         return False
#
#     def __repr__(self):
#         """
#         DO NOT EDIT
#         String representation of a node
#         :return: string of value
#         """
#         return str(self.value)


class Heap:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self, size=0):
        """
        Creates an empty hash table with a fixed capacity
        :param capacity: Initial size of the hash table.
        """
        self._array = [size]
        self._size = size


    def __str__(self):
        """
        Prints the elements in the hash table
        :return: string
        """
        return self._array


    ###### COMPLETE THE FUNCTIONS BELOW ######

    def get_size(self):
        """
        Returns number of items currently in the hash table
        :return: int: number of items in the hash table
        """
        return self._size

    def get_capacity(self):
        """
        Returns the number of indices in the hash table array
        :return: int: capacity of the array
        """
        return self._capacity

    def is_empty(self):
        """
        Returns True is the hash table is empty, false if it is not
        :return: boolean
        """
        return not self._size

    def load_factor(self):
        """
        Calculates and returns the load factor of the hash table
        :return: float: load factor
        """
        return self._size / self._capacity

    def key_hasher(self, key):
        """
        Hashes the passed in key and returns an index into the hash table array
        :param key: the key to be hashed
        :return: int: index into the hash table array
        """
        return int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16) % self._capacity

    def insert(self, key, value):
        """
        Adds value to the hash table through use of key_hasher
        :param key: the key of the value to be added
        :param value: the value to be added into the hash table
        :return: none
        """

        self._size += 1

        if not self.load_factor() < 1:
            self.grow()

        hash_index = self.key_hasher(key)
        if not self._table[hash_index]:
            self._table[hash_index] = Node(key, value)
        else:
            old_head = self._table[hash_index]
            self._table[hash_index] = Node(key, value, old_head)

    def grow(self):
        """
        Grows the hash table by doubling the size and rehashing the values into the new table
        :return: none
        """
        new_table = HashTable(self._capacity*2)
        for element in range(self._capacity):
            if self._table[element]:
                tracking_node = self._table[element]
                while tracking_node:
                    new_table.insert(tracking_node.key, tracking_node.value)
                    tracking_node = tracking_node.next_node

        self._capacity = new_table._capacity
        self._table = new_table._table

    def remove(self, key):
        """
        Removes element associated with the key
        :param key: key of the element to be deleted
        :return: none
        """
        hash_index = self.key_hasher(key)
        if not self._table[hash_index]:
            return
        else:
            if not self._table[hash_index].next_node and self._table[hash_index].key == key:
                self._table[hash_index] = 0

            elif not self._table[hash_index].next_node and self._table[hash_index].key != key:
                return

            else:
                current_node = self._table[hash_index]
                tracking_node = current_node

                while current_node.key != key:
                    tracking_node = current_node
                    current_node = current_node.next_node

                if current_node == tracking_node:
                    if current_node.next_node:
                        self._table[hash_index] = current_node.next_node
                    else:
                        self._table[hash_index] = 0

                elif current_node.key != key:
                    return

                else:
                    next_node_reference = current_node.next_node
                    tracking_node.next_node = next_node_reference

        self._size -= 1

    def getter(self, key):
        """
        If the key exists in the table, returns the value associated with it
        :param key: key of the value to be returned
        :return: value associated with the key
        """
        hash_index = self.key_hasher(key)
        if not self._table[hash_index]:
            return

        else:
            tracking_node = self._table[hash_index]
            while tracking_node:
                if tracking_node.key == key:
                    return tracking_node.value

                tracking_node = tracking_node.next_node

    def string_verify(self, key, value):
        """
        If the key value pair exists in the hash table, returns true. Otherwise returns false
        :param key: key in the key-value pair
        :param value: value in the key-value pair
        :return: boolean: if the key-value pair exists or not
        """
        if self.getter(key):
            if self.getter(key) == value:
                return True
            else:
                return False
        else:
            return False



