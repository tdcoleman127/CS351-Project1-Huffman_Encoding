testDict = {}
hcodename = "newone-hcp.txt"

# Opening up the -hcp.txt file to read
file1 = open(hcodename, "r")
for line in file1:
    print(line)
    # Split by four spaces in file
    scanningBox = line.split("    ")
    print(scanningBox)
    # Convert string version of ASCII value 
    # to int, then to str, to get original char
    newWord = chr(int(scanningBox[0])) + " with value " + scanningBox[1]
    print("New word: " + newWord)
    # Adding to a created dictionary of ASCII keys and Huffman Code values
    testDict[chr(int(scanningBox[0]))] = scanningBox[1].rstrip('\n')
file1.close()

# Verifying results
print(testDict)

# Check for characters in the original file
fname = "newone.txt"
encodedStr = ""
file2 = open(fname, "r")
for line in file2:
    for char in line:
        if char in testDict:
            print(char + " was found")
            # Finding the Huffman value for the 
            # char's key in the dictionary
            huffVal = testDict[char]
            encodedStr2 += huffVal
print(encodedStr)
file2.close()

# Creating new filename with "-hec"
nameBox = fname.split(".")
newName = nameBox[0] + "-hec." + nameBox[1]

# Writing to new file
new_file = open(newName, "w")
new_file.write(encodedStr)
new_file.close()
