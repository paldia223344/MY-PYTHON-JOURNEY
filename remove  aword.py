def RemoveWord(words,word):
    if word in words:
        words.remove(word)
        return words
    else:
        print("Word not found in words")
    
words = input("Enter  a list of word").split()
word = input("Enter a word to be  removed ")

print(RemoveWord(words,word))