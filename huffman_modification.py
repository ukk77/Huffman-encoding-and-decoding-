"author = Uddesh Karda"

import collections as c
import queue as q
from Node import *
import random as r
import time

codes = {}
modified_freq = {
        "a":8.2, "b":1.0636, "c":2.8, "d":4.3, "e":12.7, "f":1.0636, "g":1.0636, "h":6.1, "i":7.0, "j":1.0636, "k":1.0636,
        "l":4.0, "m":2.4,
        "n": 6.7, "o": 7.5, "p": 1.0636, "q": 1.0636, "r": 6.0, "s": 6.3, "t": 9.1, "u": 2.8, "v": 1.0636, "w": 2.4,
        "x": 1.0636, "y": 1.0636,"z": 1.0636
    }

def main_caller():
    for i in range(1,51,1):
        modified(i)

def modified(i):
    """
    Main function where all other methods are called
    :return: -
    """
    j = 0
    t = 0
    # n = int(input("Enter a number between 1 and 50: "))
    fw = open("modified_results.txt", 'w')
    f = open("tester")
    startTime = time.time()
    f.seek(i)
    text = f.readline()
    while j < 10:
        if text != None and text != "":
            text.lower()
            q = freq_maker_mod(text)
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
        j+=1
        if j==9:
            fw.write("test case - ")
            fw.write("\n")
            fw.write("text to encode is : " + text)
            fw.write("\n")
            fw.write(encoded)
            fw.write("\n")
            fw.write("decoded text is : " + decoded)
            fw.write("\n")
            fw.write("old length = " + str(len(text) * 8) + " bits")
            fw.write("\n")
            fw.write("new length = " + str(len(encoded) + (len(codes.keys()) * 8) + length_vals) + " bits")
            fw.write("\n")
            fw.write("compression ratio = " + str(
                ((len(encoded) + (len(codes.keys()) * 8) + length_vals) / (len(text) * 8)) * 100) + "%")
            fw.write("\n")
            fw.write("time = " + str(t/10))
            fw.write("\n")
            fw.write(" ")
            fw.write("\n")
            fw.close()
            f.close()


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


def freq_maker_mod(s):
    """
    Find all the distinct aplhabets in the text
    :param s:
    :return: Priority queue
    """
    for c in s:
        if c not in modified_freq:
            modified_freq[c] = 1
        else:
            modified_freq[c] = modified_freq[c] + 1

    pq = q.PriorityQueue()
    for key, value in modified_freq.items():
        pq.put((value, key))
    return pq


if __name__ == '__main__':
    main_caller()