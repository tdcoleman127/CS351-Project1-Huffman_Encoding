testDict = {}
hcodename = "runner-hcp.txt"

# Opening up the -hcp.txt file to read
file1 = open(hcodename, "r")
for line in file1:
    print(line)
    # Split by four spaces in file
    scanningBox = line.split("    ")
    print(scanningBox)
    newWord = scanningBox[1] + " with value " + chr(int(scanningBox[0]))
    print("New word: " + newWord)
    # Adding to a created dictionary of Huffman Code keys and ASCII character values
    testDict[scanningBox[1].rstrip('\n')] = chr(int(scanningBox[0]))
file1.close()

# Verifying results
print(testDict)

# Decoding a string by scanning the encoded string
# and comparing it with dictionary contents
fname = "runner-hec.txt"
decodedStr = ""
scanningStr = ""
file2 = open(fname, "r")
for line in file2:
    for char in line:
        # Add the current character to the scanning string
        scanningStr += char
        print(scanningStr + " is currently being scanned")
        # If the scanning string is found in the dictionary
        if scanningStr in testDict:
            print(scanningStr + " was found in dict")
            # add it to the decoded string
            # and empty the scanning string to find something else
            decodedStr += testDict[scanningStr]
            scanningStr = ""

print(decodedStr)
file2.close()

# Creating new filename with "-hdc"
nameBox = fname.split("-hec.")
newName = nameBox[0] + "-hdc." + nameBox[1]

# Writing to new file
new_file = open(newName, "w")
new_file.write(decodedStr)
new_file.close()
