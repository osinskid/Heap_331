########################################
# PROJECT XXX - Hash Table
# Author:
# PID:
########################################
import hashlib

class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'key', 'value', 'next_node'

    def __init__(self, key, value, next_node=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.key = key
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node

    def __eq__(self, other):
        """
        DO NOT EDIT
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.value == other.value and self.key == other.key:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)


class HashTable:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self, capacity=19):
        """
        Creates an empty hash table with a fixed capacity
        :param capacity: Initial size of the hash table.
        """
        self._capacity = capacity
        self._table = [0] * self._capacity
        self._size = 0

    def __str__(self):
        """
        Prints the elements in the hash table
        :return: string
        """
        if self._capacity == 0:
            return "Empty Hash Table"

        output = ""
        for element in range(self._capacity):
            if self._table[element]:
                tracking_node = self._table[element]
                output += ("Key: " + str(element) + ", Value(s): ")
                while tracking_node:
                    output += (str(tracking_node.value) + " ")
                    tracking_node = tracking_node.next_node
                output += "\n"

        return output

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def get_size(self):
        pass

    def get_capacity(self):
        pass

    def is_empty(self):
        pass

    def load_factor(self):
        pass

    def key_hasher(self, key):
        pass

    def insert(self, key, value):
        pass

    def grow(self):
        pass

    def remove(self, key):
        pass

    def getter(self, key):
        pass

    def string_verify(self, key, value):
        pass



