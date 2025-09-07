# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 18:27:24 2025

@author: Trenton C
"""

import heapq

# Node class for Huffman Tree
# Tree traversal derived from GeeksforGeeks website example
# Reference: https://www.geeksforgeeks.org/python/binary-tree-in-python/

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    # Defined comparison for nodes "less than" logic
    def __lt__(self, other):
        return self.val < other.val

# Note: Based in-order traversal from instruction pdf example and GeeksforGeeks pages on Huffman Encoding and Tree Traversal
# Reference 1: https://www.geeksforgeeks.org/dsa/huffman-coding-greedy-algo-3/
# Reference 2: https://www.geeksforgeeks.org/dsa/inorder-traversal-of-binary-tree/

def goInOrder(node, final, currentStr):
    if node is None:
        return
    # Add "0" to currentStr for going left in tree
    goInOrder(node.left, final, currentStr + '0')

    # If the node is an internal node
    if(node.key == "IN"):
        print("Internal Node")
        print(node.val)
    else:
        # If the node is an character node
        print("Character Node for: " + node.key)
        print(node.val)

        # Add the path to the character node to the overall list
        # print("The string being added is: " + currentStr)
        new_tuple = (node.key, currentStr)
        final.append(new_tuple)
        # print(final)

    # Add "1" to currentStr for going left in tree
    goInOrder(node.right, final, currentStr + '1')


# functions for Step 1
def getFrequencyCounts(fname):
    myDict = {}
    # Open file
    file = open(fname, 'r')
    
    # Read file char by char, line by line
    for line in file:
        for char in line:
            if char not in myDict:
                # if char not found, create key and give value 1
                myDict[char] = 1
            else:
                # if found, increment frequency value
                myDict[char] += 1
    file.close()
    print("The dictionary of frequency counts for " + fname + " is: ")
    
    # Sorting dictionary values by value, ascending
    newDict = dict(sorted(myDict.items(), key=lambda x:x[1]))
    print(newDict)
    return newDict

def buildHuffmanCodeTree(freqCounts):
    # Initializing min_heap and heapify()-ing it
    min_heap = []
    heapq.heapify(min_heap)   

    # Initalizing tree nodes with character frequency values
    for c in freqCounts:
        print("Initializing node: " + c)
        print("Character frequency value: ")
        print(freqCounts[c])
        initialNode = Node(c, freqCounts[c])
        # Pushing initialNode to min_heap
        heapq.heappush(min_heap, initialNode)
    
    while len(min_heap) > 1:
        # print(priority_queue)
        f1 = heapq.nsmallest(1, min_heap)[0]
        t1 = heapq.heappop(min_heap)
        f2 = heapq.nsmallest(1, min_heap)[0]
        t2 = heapq.heappop(min_heap)

        # Creating the linking node with combined value
        print("Creating linking node:")
        linkingVal = f1.val + f2.val
        print(linkingVal)
        print("----------")
        linkingNode = Node("IN", linkingVal)
        linkingNode.left = t1
        linkingNode.right = t2

        # Pushing the linking node to the next iteration of the min_heap
        heapq.heappush(min_heap, linkingNode)

    # print(min_heap)
    # Returning root node of created tree
    # Can verify by checking for internal node key "IN"
    root = heapq.heappop(min_heap)
    print("The root node should be: ")
    print(root.val)
    print("Verified with internal node key: " + root.key)
    print("----------")
    return root

def getHuffmanCodes(huffTree):
    tuplesList = []
    currentStr = ""

    # In-order traversal function
    # to encode values for all characters in tree
    goInOrder(huffTree, tuplesList, currentStr)
    print("The final Huffman array before and after sorting: ")
    print(tuplesList)

    # Sorting list of tuples by key, ASCII characters, ascending order
    tuplesList.sort(key=lambda item: item[0])
    print(tuplesList)
    
    # Return generated list of tuples
    return tuplesList

def determineHuffmanCode(fname):
    # Functions to get Huffman Code info
    freqDict = getFrequencyCounts(fname)
    huffTree = buildHuffmanCodeTree(freqDict)
    huffCodes = getHuffmanCodes(huffTree)

    # Creating new filename with "-hcp"
    boxed = fname.split(".")
    newName = boxed[0] + "-hcp." + boxed[1]

    # Writing to new file
    new_file = open(newName, "w")
    for item in huffCodes:
        new_file.write(str(ord(item[0])) + "    " + item[1] + "\n")

    # Closing newly created file
    new_file.close()
    return newName

# function for Step 2
def convertToHuffman(fname, hcodename):
    fileToConvert = fname
    huffCodeTuples = hcodename
    encodedStr = ""
    
    # Read file char by char, line by line
    for line in fname:
        for char in line:
            for item in huffCodeTuples:
                if char == item[0]:
                    encodedStr += item[1]

    print(encodedStr)

    # Creating new filename with "-hcp"
    boxed = fname.split(".")
    newName = boxed[0] + "-hec." + boxed[1]


    # Writing to new file
    new_file = open(newName, "w")
    new_file.write(encodedStr)

    return newName
    pass

# function for Step 3
def convertFromHuffman(encodedname, hcodename):
    pass


def cs351Proj1():
    fname = input("Enter filename\n")
    print ("Original File name:", fname)
    
    hcodename = determineHuffmanCode(fname)
    print ("Huffman Code File name:", hcodename)
    
    # encodedname = convertToHuffman(fname, hcodename)
    # print ("Huffman Encoded File name:", encodedname)
    
    # decodedname = convertFromHuffman(encodedname, hcodename)
    # print ("Final/Decoded File name:", decodedname)
    
#call main function
cs351Proj1()
    