# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 18:27:24 2025

@author: troy
"""

# functions for Step 1
def getFrequencyCounts(fname):
    pass

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
    
    hcodename = determineHuffmanCode(fname)
    print ("Huffman Code File name:", hcodename)
    
    encodedname = convertToHuffman(fname, hcodename)
    print ("Huffman Encoded File name:", encodedname)
    
    decodedname = convertFromHuffman(encodedname, hcodename)
    print ("Final/Decoded File name:", decodedname)
    
#call main function
cs351Proj1()
    