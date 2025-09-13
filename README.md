# CS351-Project1-Huffman_Encoding

This is my repository for my CS 351 Course Project #1 on Huffman Encoding. This code will prompt you to enter a filename, and generate Huffman encoded and decoded .txt files for your reference.

This is written in Python, primarily using the heapq library for functionality.

Within the repository are my test files to test once you run:

**python proj1tcole21.py**

in your terminal.

Next, the terminal will prompt you to enter a filename:

**Enter filename:**
**(Your file here)**

Note: This works assuming you use a .txt file

Some example .txt files are provided for you to use:

none.txt - an empty file
single.txt - a file with one character
couple.txt - a file with two characters
letters.txt - a file with a's, b's, and c's in one line
sentence.txt - a file containing a sentence
random_characters.txt - a file of random characters across multiple lines

As also listed in terminal, and in your repository if you choose to clone or fork this, you'll have .txt files generated

Example:
document.txt - your file with text
document-hcp.txt - file containing ASCII to Huffman Code pairs
document-hec.txt - Huffman encoding of document.txt's text
document-hdc.txt - Decoded version of document-hec.txt, identical to document.txt