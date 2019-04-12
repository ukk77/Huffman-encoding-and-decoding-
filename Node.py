"author = Uddesh Karda"

class Node:
    __slots__ = 'left', 'data', 'right', 'frequency'

    def __init__(self, data = 'freq_node', frequency = 0, left=None, right=None):
        """
        Constructor for node Class
        :param data: The string data
        :param frequency: Frequency count of the alphabet
        :param left: Left node
        :param right: right node
        """
        self.data = data
        self.left = left
        self.right = right
        self.frequency = frequency

    def __lt__(self, other):
        """
        Comparision method
        :param other:
        :return: Boolean
        """
        return self.frequency <= other.frequency