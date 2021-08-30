def countWordsFromFile():
    fileName = input("Enter Name Of File")
    numberOfWord = 0
    file = open(fileName,'r')
    for line in file:
        words = line.split()
        numberOfWord = numberOfWord + len(words)
    print("Number Of Words:")
    print(numberOfWord)


countWordsFromFile()