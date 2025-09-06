# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 18:27:24 2025

@author: troy
"""

import heapq
import os

# Node class for Huffman Tree
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.val < other.val

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
    print(myDict)
    return myDict

def buildHuffmanCodeTree(freqCounts):
    # Get the dictionary of frequency counts
    # And initialize priority queue (MUST heapify first!)
    priority_queue = []
    heapq.heapify(priority_queue)

    #Initalizing priority queue

    for c in freqCounts:
        print("Initializing node: " + c)
        print("Character frequency value: ")
        print(freqCounts[c])
        T = Node(c, freqCounts[c])
        heapq.heappush(priority_queue, T)
    
    while len(priority_queue) > 1:
        f1 = heapq.nsmallest(1, priority_queue)[0]
        t1 = heapq.heappop(priority_queue)
        f2 = heapq.nsmallest(1, priority_queue)[0]
        t2 = heapq.heappop(priority_queue)

        # Creating the linking node
        print("Creating linking node")
        print("Linking node with associated value")
        print(f1.val + f2.val)
        T = Node("IN", f1.val + f2.val)
        T.left = t1
        T.right = t2

        # Pushing the linking node to the next iteration of the min heap
        heapq.heappush(priority_queue, T)

    # print(priority_queue)
    return heapq.heappop(priority_queue)
    pass

def getHuffmanCodes(huffTree):
    pass

def determineHuffmanCode(fname):
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
    freqDict = getFrequencyCounts(fname)
    buildHuffmanCodeTree(freqDict)
    
    hcodename = determineHuffmanCode(fname)
    print ("Huffman Code File name:", hcodename)
    
    encodedname = convertToHuffman(fname, hcodename)
    print ("Huffman Encoded File name:", encodedname)
    
    decodedname = convertFromHuffman(encodedname, hcodename)
    print ("Final/Decoded File name:", decodedname)
    
#call main function
cs351Proj1()
    