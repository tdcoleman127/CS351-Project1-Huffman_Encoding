testDict = {}
hcodename = "newone-hcp.txt"
encodedStr = ""

# Opening up the -hcp.txt file to read
file1 = open(hcodename, "r")
for line in file1:
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
    # encodedStr += boxed[1].rstrip('\n')
file1.close()

# Verifying results
print(testDict)
print("Encoded string: " + encodedStr)

# Do for the original file
fname = "newone.txt"
encodedStr2 = ""
file2 = open(fname, "r")
for line in file2:
    for char in line:
        if char in testDict:
            # print(char)
            print(char + " was found")
            huffVal = testDict[char]
            encodedStr2 += huffVal
print(encodedStr2)


# Creating new filename with "-hec"
boxed = ""
boxed = fname.split(".")
newName = boxed[0] + "-hec." + boxed[1]
# Writing to new file
new_file = open(newName, "w")
new_file.write(encodedStr2)
new_file.close()
