import sys

from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QListWidget, QLineEdit, QLabel

#from main import Board

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.win_w: int = 500
        self.win_h: int = 300

        self.buf_w: int = 20
        self.buf_h: int = 10

        self.initUI()   


    def initUI(self):

        grid = QGridLayout(self)
        grid.setGeometry(QRect(self.buf_w, self.buf_h, self.win_w-2*self.buf_w, self.win_h-2*self.buf_h))
        
        btn_clear = QPushButton('Clear', self)
        btn_a = QPushButton("Algorithm A", self)
        btn_b = QPushButton("Algorithm B", self)
        btn_best = QPushButton("Best Algorithm", self)

        word_list = QListWidget(self)
        letter_list = QListWidget(self)

        word_input = QLineEdit(self)
        word_input.setPlaceholderText("Enter words here")
        letter_input = QLineEdit(self)
        letter_input.setPlaceholderText("Number of letters")

        word_label = QLabel("Word List:", self)
        letter_label = QLabel("Optimal Letters:", self)

        grid.addWidget(word_input, 1, 0)
        grid.addWidget(letter_input, 0, 1)
        grid.addWidget(btn_clear, 1, 1)
        grid.addWidget(btn_a, 0, 2)
        grid.addWidget(btn_b, 1, 2)
        grid.addWidget(btn_best, 2, 2)
        grid.addWidget(word_label, 2, 0, 1, 2)
        grid.addWidget(letter_label, 3, 2)
        grid.addWidget(word_list, 3, 0, 3, 2)
        grid.addWidget(letter_list, 4, 2, 2, 1)

        
        self.resize(self.win_w, self.win_h)
        self.center()

        self.setWindowTitle("Crossword Scratcher Optimizer")
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    
    app = QApplication(sys.argv)

    win = Window()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
