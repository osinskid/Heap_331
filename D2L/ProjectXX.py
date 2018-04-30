########################################
# PROJECT XXX - Min Heap and Sort
# Author:
# PID:
########################################


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
        pass

    def parent(self, i):
        pass

    def left(self, i):
        pass

    def right(self, i):
        pass

    def has_left(self, i):
        pass

    def has_right(self, i):
        pass

    def insert(self, value):
        pass

    def remove(self, value):
        pass

    def swap(self, i, j):
        pass

    def upheap(self, i):
        pass

    def downheap(self, i):
        pass

    def remove_min(self):
        pass


def heapSort(unsorted):
    pass


def getStats(unsorted):
    pass
