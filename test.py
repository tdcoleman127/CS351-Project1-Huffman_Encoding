# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 18:27:24 2025

@author: troy
"""

import heapq
import os
import operator

# Node class for Huffman Tree
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.val < other.val
    
def goInOrder(node, final, currentStr):
    if node is None:
        return
    
    goInOrder(node.left, final, currentStr + '0')

    # If the node is an internal node
    if(node.key == "IN"):
        print("Internal Node")
        print(node.val)
    else:
        # If the node is an character node
        print("Character Node for: " + node.key)
        print(node.val)

        # Add the path to the character node to the overall array
        # print("The string being added is: " + currentStr)
        new_tuple = (node.key, currentStr)
        final.append(new_tuple)
        print(final)

    goInOrder(node.right, final, currentStr + '1')


# functions for Step 1
def getFrequencyCounts(fname):
    myDict = {}
    file = open(fname, 'r')
    for line in file:
        for char in line:
            if char not in myDict:
                myDict[char] = 1
            else:
                myDict[char] += 1
    file.close()
    print("The dictionary of frequency counts for " + fname + " is: ")
    
    newDict = dict(sorted(myDict.items(), key=lambda x:x[1]))
    print(newDict)
    return newDict

def buildHuffmanCodeTree(freqCounts):
    # Initialize priority queue (MUST heapify first!)
    priority_queue = []
    heapq.heapify(priority_queue)   

    # Initalizing tree nodes with character frequency values
    for c in freqCounts:
        print("Initializing node: " + c)
        print("Character frequency value: ")
        print(freqCounts[c])
        T = Node(c, freqCounts[c])
        heapq.heappush(priority_queue, T)
    
    while len(priority_queue) > 1:
        # print(priority_queue)
        f1 = heapq.nsmallest(1, priority_queue)[0]
        t1 = heapq.heappop(priority_queue)
        f2 = heapq.nsmallest(1, priority_queue)[0]
        t2 = heapq.heappop(priority_queue)

        # Creating the linking node
        print("Creating linking node:")
        print(f1.val + f2.val)
        print("----------")
        T = Node("IN", f1.val + f2.val)
        T.left = t1
        T.right = t2

        # Pushing the linking node to the next iteration of the min heap
        heapq.heappush(priority_queue, T)

    # print(priority_queue)
    root = heapq.heappop(priority_queue)
    print("The root node should be: ")
    print(root.val)
    print("Verified with internal node key: " + root.key)
    print("----------")
    return root
    pass

def getHuffmanCodes(huffTree):
    final = []
    currentStr = ""
    goInOrder(huffTree, final, currentStr)
    print("The final huffman array should be: ")
    print(final)
    return final
    pass

def determineHuffmanCode(fname):
    freqDict = getFrequencyCounts(fname)
    freqTree = buildHuffmanCodeTree(freqDict)
    final = getHuffmanCodes(freqTree)

    # Creating new file
    filename = fname + "-hcp"
    new_file = open(filename + ".txt", "w")
    for item in final:
        new_file.write(str(ord(item[0])) + "  " + item[1] + "\n")
    new_file.close()
    return filename + ".txt"
    pass

# function for Step 2
def convertToHuffman(fname, hcodename):
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
    