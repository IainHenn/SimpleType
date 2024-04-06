from sentences import words 

wordsTXT = r"words.txt"
sentence = []
setOfWords = []
obj1 = words(setOfWords,sentence)
obj1.addWords(wordsTXT)
obj1.create_sentence()
obj1.getSentence()
obj1.printSentence()