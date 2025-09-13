word = "document.txt"
print("Original word: " + word)
boxed = word.split(".")
print(boxed)
newWord = boxed[0] + "-hcp." + boxed[1]
print("New word: " + newWord)