message = input("TYPE HERE")
characterCount = 0
wordCount = 1
for a in message:
    characterCount = characterCount + 1
    if(a == " "):
        wordCount = wordCount + 1
print("number of words in the string:")
print(wordCount)
print("number of characters in the string:")
print(characterCount)