from sentences import words 
from tkinter import *
import random 
import time

wordsTXT = r"WPM Program/words.txt"
sentence = []
setOfWords = []
global testArr
global randomWord
global i
global startTime
global wpm
global timeElapsed

i = 0
#testArr = ["start","spider", "finger", "who", "house", "their"]
#testArr_no_start = ["spider","finger","who","house","their"]
startTime = 0
timeElapsed = 0
wpm = 0

obj1 = words(setOfWords,sentence)
obj1.addWords(wordsTXT)
obj1.create_sentence()
wordsArr = obj1.getSentence()
randomWord = wordsArr[i]
print(wordsArr)

mainWindow = Tk()
mainWindow.minsize(900,300)
mainWindow.title("SimpleType")

def totalKeys(array):
    keys = 0
    for i in array:
        keys += len(i)
    return keys

def greetingFunc():
    global greeting
    greeting = Label(mainWindow,width = 500, text = "Type \"start\" To Begin")
    greeting.config(font = ('Arial',26))
    greeting.pack(padx = 10, pady = 10)

def postWPM():
    global WPM_lab
    WPM_lab = Label(mainWindow,width = 500, text = str(round((totalKeys(wordsArr)/5)/(timeElapsed/60),2))+ " WPM")
    WPM_lab.config(font = ('Arial',26))
    WPM_lab.pack(padx = 10, pady = 10)

def rWordFunc():
    global word
    word = Label(mainWindow, width = 500, text = randomWord)
    word.config(font = ('Arial',26))
    word.pack(padx = 10, pady = 10)

def entry():
    global textBox
    textBox = Entry(mainWindow, width = 500, bd = 5, justify = 'center')
    textBox.config(font = ('Arial',30))
    textBox.bind("<Return>",enterPressed)
    textBox.focus_set()
    textBox.pack(side = BOTTOM)

def updateWord(word):
    global randomWord
    word.config(text = randomWord)

def enterPressed(event):
   global randomWord
   global i
   global word
   print(textBox.get() == randomWord)
   if(textBox.get() == randomWord):
       if(randomWord == "start"):
           startTime()
           textBox.delete(0,"end")
       textBox.delete(0,"end")
       i = i + 1
       if(i < len(wordsArr)):
            randomWord = wordsArr[i]
            updateWord(word)
       else:
           endTime()
           postWPM()
               
            

def startTime():
    global startTime 
    startTime = time.time()
    print("Start Time: " + str(startTime))

def endTime():
    global timeElapsed
    endTime = time.time()
    timeElapsed = endTime - startTime
    

while True:
    greetingFunc()
    rWordFunc()
    entry()
    mainWindow.mainloop()
