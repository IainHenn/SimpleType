import random



class words:
    def __init__(self,w,sentence):
        self._wordsArr = w
        self._sentenceArr = sentence
    
    def getWordsArr(self):
        return self._wordsArr
    
    def setWordsArr(self, newWordsArr):
        self._wordsArr = newWordsArr
    
    def printWordsArr(self):
        print(self.getWordsArr())

    def addWords(self,textFile):
        tempWordsArr = []
        file = open(textFile,"r")
        for word in file:
            word = word.strip("\n")
            tempWordsArr.append(word)
        self.setWordsArr(tempWordsArr)

    def getSentence(self):
        return self._sentenceArr
    
    def setSentence(self,newSentence):
        self._sentenceArr = newSentence

    def printSentence(self):
        print(self.getSentence())
    
    def create_sentence(self):
        random.seed()
        tempSentenceArr = []
        for i in range(1,10):
            tempSentenceArr.append(self.getWordsArr()[random.randint(0,len(self.getWordsArr()))])
        tempSentenceArr.insert(0,"start")
        self.setSentence(tempSentenceArr)

