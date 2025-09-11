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
        # print("Internal Node")
        # print(node.val)
        pass
    else:
        # If the node is an character node
        # print("Character Node for: " + node.key)
        # print(node.val)

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
    # if file.size() ==

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

    # Base case: file with only a single character
    if(len(min_heap) == 0):
        print("No characters available")
        linkingNode = Node("IN", 0)
        heapq.heappush(min_heap, linkingNode)
    if(len(min_heap) == 1):
        print("Length of min heap is 1, running alternative algorithm")
        t1 = heapq.heappop(min_heap)
        linkingVal = 1
        linkingNode = Node("IN", linkingVal)
        linkingNode.left = t1
        heapq.heappush(min_heap, linkingNode)
    # All other normal cases
    else:
        while len(min_heap) > 1:
            # print(priority_queue)
            f1 = heapq.nsmallest(1, min_heap)[0]
            t1 = heapq.heappop(min_heap)
            f2 = heapq.nsmallest(1, min_heap)[0]
            t2 = heapq.heappop(min_heap)

            # Creating the linking node with combined value
            # print("Creating linking node:")
            linkingVal = f1.val + f2.val
            # print(linkingVal)
            # print("----------")
            linkingNode = Node("IN", linkingVal)
            linkingNode.left = t1
            linkingNode.right = t2

            # Pushing the linking node to the next iteration of the min_heap
            heapq.heappush(min_heap, linkingNode)

    # print(min_heap)
    # Returning root node of created tree
    # Can verify by checking for internal node key "IN"
    root = heapq.heappop(min_heap)
    # print("The root node should be: ")
    # print(root.val)
    # print("Verified with internal node key: " + root.key)
    # print("----------")
    return root

def getHuffmanCodes(huffTree):
    tuplesList = []
    currentStr = ""

    # In-order traversal function
    # to encode values for all characters in tree
    goInOrder(huffTree, tuplesList, currentStr)
    # print("The final Huffman array before and after sorting: ")
    # print(tuplesList)

    # Sorting list of tuples by key, ASCII characters, ascending order
    tuplesList.sort(key=lambda item: item[0])
    # print(tuplesList)
    
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
    testDict = {}
    # Opening up the -hcp.txt file to read
    file1 = open(hcodename, "r")
    for line in file1:
        # print(line)
        # Split by four spaces in file
        scanningBox = line.split("    ")
        # print(scanningBox)
        # Convert string version of ASCII value 
        # to int, then to str, to get original char
        newWord = chr(int(scanningBox[0])) + " with value " + scanningBox[1]
        # print("New word: " + newWord)
        # Adding to a created dictionary of ASCII keys and Huffman Code values
        testDict[chr(int(scanningBox[0]))] = scanningBox[1].rstrip('\n')
    file1.close()

    # Verifying results
    print(testDict)

    # Check for characters in the original file
    encodedStr = ""
    file2 = open(fname, "r")
    for line in file2:
        for char in line:
            if char in testDict:
                # print(char + " was found")
                # Finding the Huffman value for the 
                # char's key in the dictionary
                huffVal = testDict[char]
                encodedStr += huffVal
    # print(encodedStr)
    file2.close()

    # Creating new filename with "-hec"
    nameBox = fname.split(".")
    newName = nameBox[0] + "-hec." + nameBox[1]

    # Writing to new file
    new_file = open(newName, "w")
    new_file.write(encodedStr)
    new_file.close()
    # print(newName)
    return newName

# function for Step 3
def convertFromHuffman(encodedname, hcodename):
    testDict = {}

    # Opening up the -hcp.txt file to read
    file1 = open(hcodename, "r")
    for line in file1:
        # print(line)
        # Split by four spaces in file
        scanningBox = line.split("    ")
        # print(scanningBox)
        newWord = scanningBox[1] + " with value " + chr(int(scanningBox[0]))
        # print("New word: " + newWord)
        # Adding to a created dictionary of Huffman Code keys and ASCII character values
        testDict[scanningBox[1].rstrip('\n')] = chr(int(scanningBox[0]))
    file1.close()

    # Verifying results
    # print(testDict)

    # Decoding a string by scanning the encoded string
    # and comparing it with dictionary contents
    decodedStr = ""
    scanningStr = ""
    file2 = open(encodedname, "r")
    for line in file2:
        for char in line:
            # Add the current character to the scanning string
            scanningStr += char
            # print(scanningStr + " is currently being scanned")
            # If the scanning string is found in the dictionary
            if scanningStr in testDict:
                # print(scanningStr + " was found in dict")
                # add it to the decoded string
                # and empty the scanning string to find something else
                decodedStr += testDict[scanningStr]
                scanningStr = ""

    # print(decodedStr)
    file2.close()

    # Creating new filename with "-hdc"
    nameBox = encodedname.split("-hec.")
    newName = nameBox[0] + "-hdc." + nameBox[1]

    # Writing to new file
    new_file = open(newName, "w")
    new_file.write(decodedStr)
    new_file.close()
    return newName
    pass


def cs351Proj1():
    fname = input("Enter filename\n")
    print ("Original File name:", fname)
    
    hcodename = determineHuffmanCode(fname)
    print ("Huffman Code File name:", hcodename)
    
    encodedname = convertToHuffman(fname, hcodename)
    print ("Huffman Encoded File name:", encodedname)
    
    decodedname = convertFromHuffman(encodedname, hcodename)
    print ("Final/Decoded File name:", decodedname)
    
#call main function
cs351Proj1()
    