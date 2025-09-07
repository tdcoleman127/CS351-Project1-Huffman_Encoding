testDict = {}
hcodename = "runner-hcp.txt"
encodedStr = ""

# Opening up the -hcp.txt file to read
file = open(hcodename, "r")
for line in file:
    print(line)
    # Split by four spaces in file
    boxed = line.split("    ")
    print(boxed)
    # Convert string version of ASCII value 
    # to int, then to str, to get original char
    newWord = chr(int(boxed[0])) + " with value " + boxed[1]
    print("New word: " + newWord)
    # Adding to a created dictionary of ASCII keys and Huffman Code values
    testDict[chr(int(boxed[0]))] = boxed[1].rstrip('\n')
    encodedStr += boxed[1].rstrip('\n')
file.close()

print(testDict)
print("Encoded string: " + encodedStr)


# boxed = fname.split("    ")
# newName = boxed[0] + "-hcp." + boxed[1]
# # Create a ke
# pairDict[boxed[0]] = boxed[1]