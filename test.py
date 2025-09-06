# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 18:27:24 2025

@author: troy
"""

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
    print(myDict)
    return myDict

def buildHuffmanCodeTree(freqCounts):
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
    fname = input("Enter filename")
    print ("Original File name:", fname)
    getFrequencyCounts(fname)
    
    hcodename = determineHuffmanCode(fname)
    print ("Huffman Code File name:", hcodename)
    
    encodedname = convertToHuffman(fname, hcodename)
    print ("Huffman Encoded File name:", encodedname)
    
    decodedname = convertFromHuffman(encodedname, hcodename)
    print ("Final/Decoded File name:", decodedname)
    
#call main function
cs351Proj1()
    