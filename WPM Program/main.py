from sentences import words 
from PySide6 import QtCore, QtWidgets, QtGui
import sys 
import random 

wordsTXT = r"words.txt"
sentence = []
setOfWords = []



#obj1 = words(setOfWords,sentence)
#obj1.addWords(wordsTXT)
#obj1.create_sentence()
#obj1.getSentence()
#obj1.printSentence()



class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SimpleType")
        self.kod = []
        self.button = QtWidgets.QPushButton("Press Space To Start")
        lay = QtWidgets.QVBoxLayout(self)
        lay.setContentsMargins(300,300,300,300)
        lay.addStretch()
        lay.addWidget(self.button, alignment = QtCore.Qt.AlignVCenter)

        self.button.clicked.connect(self.clearLayout)







if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Main()
    widget.resize(900,600)
    widget.show()

    sys.exit(app.exec())
