"author = Uddesh Karda"

import collections as c
import queue as q
from Node import *
import random as r
import time

letter_count = {}
codes = {}
modified_freq = {}


def main():
    """
        Main function where all other methods are called
        :return: -
        """
    t = 0
    n = int(input("Enter a number between 1 and 50: "))
    f = open("tester")
    startTime = time.time()
    f.seek(n)
    text = f.readline()
    if text != None and text != "":
        q = freq_maker(text)
        nodes = leaf_node_make(q)
        root = code_make(nodes)
        find_code(root, [])
        encoded = encoder(text)
        length_vals = 0
        for val in codes.values():
            length_vals += len(val)
        decoded = decoder(encoded)
    else:
        print("empty text string")
    endTime = time.time()
    t += endTime - startTime
    print("text to encode is : " + text)
    print(encoded)
    print("decoded text is : " + decoded)
    print("old length = " + str(len(text) * 8) + " bits")
    print("new length = " + str(len(encoded) + (len(codes.keys()) * 8) + length_vals) + " bits")
    print("compression ratio = " + str(
        ((len(encoded) + (len(codes.keys()) * 8) + length_vals) / (len(text) * 8)) * 100) + "%")
    print("time = " + str(t / 10))



def encoder(text):
    """
        Replaces each alphabet by its code
        :param text:
        :return: Encoded String
        """
    encoded_text = ""
    for c in text:
        encoded_text+=codes.get(c)
    return encoded_text


def decoder(encoded_string):
    """
        Convert encoded text to English language
        :param encoded_string:
        :return: Decoded String
        """
    rev_count = {}
    decoded_text = ""
    for key, value in codes.items():
        rev_count[value] = key
    i = 0
    while i <= len(encoded_string):
        if encoded_string[:i] in rev_count:
            decoded_text += rev_count.get(encoded_string[:i])
            encoded_string = encoded_string[i:]
            i = 0
        else:
            pass
        i += 1
    return decoded_text


def find_code(root, stack):
    """
        Function to build codes for alphabets by traversing tree
        :param root: The root node of the tree
        :param stack: List
        :return: -
        """
    if root.left == None and root.right == None:
        if root.data == 'freq_node':
            return
        else:
            code = ''
            for i in range(len(stack)):
                code += str(stack[i])
            codes[root.data] = code
            return
    else:
        if root.left!=None:
            stack.append(0)
            find_code(root.left,stack)
            stack.pop()
        if root.right!=None:
            stack.append(1)
            find_code(root.right,stack)
            stack.pop()


def code_make(nodes):
    """
        Function to build Huffman tree
        :param nodes: List of nodes
        :return: Root node of tree
        """
    pq = q.PriorityQueue()
    for i in range(len(nodes)):
        pq.put(nodes[i])
    while pq.qsize()!=1:
        n1 = pq.get()
        n2 = pq.get()

        new_Node = Node(frequency = n1.frequency + n2.frequency)
        new_Node.left = n1
        new_Node.right = n2

        pq.put(new_Node)
    root = pq.get()
    return root


def leaf_node_make(q):
    """
        Function to create leaf nodes for each distinct alphabet
        :param q: priority queue
        :return: List of nodes
        """
    temp_nodes = []
    while not q.empty():
        d = q.get()
        temp_nodes.append(Node(data=d[1], frequency=d[0]))
    return temp_nodes


def freq_maker(s):
    """
        Find all the distinct aplhabets in the text
        :param s:
        :return: Priority queue
        """
    for c in s:
        if c not in letter_count:
            letter_count[c] = 1
        else:
            letter_count[c] = letter_count[c] + 1

    pq = q.PriorityQueue()
    for key, value in letter_count.items():
        pq.put((value, key))
    return pq

if __name__ == '__main__':
    main()