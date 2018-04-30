########################################
# PROJECT XXX - Min Heap and Sort
# Author:
# PID:
########################################
import math


class Heap:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self, size=0):
        """
        Creates an empty hash table with a fixed capacity
        :param capacity: Initial size of the hash table.
        """
        self.array = []

    def __str__(self):
        """
        Prints the elements in the hash table
        :return: string
        """
        return str(self.array)

    def __repr__(self):
        """
        Returns the string representation
        :return: string representation of self
        """
        return str(self)

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def get_size(self):
        """
        Returns number of items currently in the hash table
        :return: int: number of items in the hash table
        """
        return len(self.array)

    def parent(self, i):
        """
        Returns the index of the parent of node at index i
        :param i: node to find the parent of
        :return: index of parent node
        """
        return (i - 1) // 2

    def left(self, i):
        """
        Returns the index of the left child of node at index i
        :param i: node to find the left child of
        :return: index of left child
        """
        return 2 * i + 1

    def right(self, i):
        """
        Returns the index of the right child of node at index i
        :param i: node to find the right child of
        :return: node of the right child
        """
        return 2 * i + 2

    def has_left(self, i):
        """
        Returns whether or not node i has a left child
        :param i: node to check left child of
        :return: boolean
        """
        return self.left(i) < len(self.array)

    def has_right(self, i):
        """
        Returns whether or not node i has a right child
        :param i: node to check right child of
        :return: boolean
        """
        return self.right(i) < len(self.array)

    def insert(self, value):
        """
        Creates a node with the value value and adds it to the heao
        :param value: value to be added
        :return: none
        """
        self.array.append(value)
        self.upheap(len(self.array) - 1)

    def remove(self, value):
        """
        Removes the node with value value
        :param value: value of node to be removed
        :return: none
        """
        value_index = self.find(value)
        if not isinstance(value_index, bool):
            self.swap(value_index, len(self.array) - 1)
            self.array.pop()
            self.downheap(value_index)
            return

    def swap(self, i, j):
        """
        Swaps the elements at indices i and j of the array
        :param i: first index
        :param j: second index
        :return: none
        """
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def upheap(self, i):
        """
        Moves node at index i up the tree via swaps until it is in the proper position
        :param i: node to upheap
        :return: none
        """
        parent = self.parent(i)
        if i > 0 and self.array[i] < self.array[parent]:
            self.swap(i, parent)
            self.upheap(parent)

    def downheap(self, i):
        """
        Moves node at index i down the tree via swaps until it is in the proper position
        :param i: node to downheap
        :return: none
        """
        if self.has_left(i):
            left = self.left(i)
            small_child = left
            if self.has_right(i):
                right = self.right(i)
                if self.array[right] < self.array[left]:
                    small_child = right
            if self.array[small_child] < self.array[i]:
                self.swap(i, small_child)
                self.downheap(small_child)

    def find(self, value):
        """
        Finds the index of the node with value value
        :param value: value to search for
        :return: the index number or False
        """
        for index in range(len(self.array)):
            if self.array[index] == value:
                return index

        return False

    def remove_min(self):
        """
        Removes and returns the root node, then updates list so it remains a MinHeap
        :return: value of node with min value
        """
        self.swap(0, len(self.array) - 1)
        item = self.array.pop()
        self.downheap(0)
        return item


def heapSort(unsorted):
    """
    Given an unsorted list, performs a Heap Sort
    :param unsorted: list to be sorted
    :return: sorted list
    """
    min_tree = Heap()
    sorted_list = []
    for element in unsorted:
        min_tree.insert(element)
    size = min_tree.get_size()
    for i in range(0, size):
        sorted_list.append(min_tree.remove_min())
    return sorted_list


def getStats(unsorted):
    """
    Given an unsorted list, returns a list of information in the following format:
    [minimum val, maximum val, mean, median, mode]
    :param unsorted: unsorted list
    :return: list containing the information about unsorted
    """
    sorted_list = heapSort(unsorted)
    frequency_dict = {}
    if isinstance(unsorted[0], int):
        mode = 0
        data_sum = 0
    else:
        mode = ""
        data_sum = ""
    max_val = 0
    for element in sorted_list:
        if element not in frequency_dict:
            frequency_dict[element] = 1
        else:
            frequency_dict[element] += 1
        data_sum += element
    for val, freq in frequency_dict.items():
        if freq > max_val:
            max_val = freq
            mode = val

    median_i = len(sorted_list) // 2
    if isinstance(unsorted[0], int):
        mean = data_sum / len(sorted_list)
    else:
        ascii_total = 0
        for c in data_sum:
            ascii_total += ord(c)
        mean = chr(ascii_total // len(data_sum))
    return [sorted_list[0], sorted_list[len(sorted_list) - 1], mean, sorted_list[median_i], mode]
