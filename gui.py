import sys

from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QListWidget, QLineEdit, QLabel

from main import Board

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.win_w: int = 600
        self.win_h: int = self.win_w*9//16

        self.buf_w: int = 20
        self.buf_h: int = self.buf_w*9//16

        self.grid = QGridLayout(self)
        
        self.btn_clear = QPushButton('Clear', self)
        self.btn_a = QPushButton("Algorithm A", self)
        self.btn_b = QPushButton("Algorithm B", self)
        self.btn_best = QPushButton("Best Algorithm", self)

        self.word_list = QListWidget(self)
        self.letter_list = QListWidget(self)

        self.word_input = QLineEdit(self)
        self.word_input.setPlaceholderText("Enter words here")
        self.letter_input = QLineEdit(self)
        self.letter_input.setPlaceholderText("Number of letters")

        self.word_label = QLabel("Word List:", self)
        self.letter_label = QLabel("Optimal Letters:", self)

        self.initUI()   


    def initUI(self):

        self.grid.setGeometry(QRect(self.buf_w, self.buf_h, self.win_w-2*self.buf_w, self.win_h-2*self.buf_h))

        self.grid.addWidget(self.word_input, 1, 0)
        self.grid.addWidget(self.letter_input, 0, 1)
        self.grid.addWidget(self.btn_clear, 1, 1)
        self.grid.addWidget(self.btn_a, 0, 2)
        self.grid.addWidget(self.btn_b, 1, 2)
        self.grid.addWidget(self.btn_best, 2, 2)
        self.grid.addWidget(self.word_label, 2, 0, 1, 2)
        self.grid.addWidget(self.letter_label, 3, 2)
        self.grid.addWidget(self.word_list, 3, 0, 3, 2)
        self.grid.addWidget(self.letter_list, 4, 2, 2, 1)

        self.btn_clear.clicked.connect(self.clear_fields)
        self.btn_a.clicked.connect(self.display_algo_a)
        self.btn_b.clicked.connect(self.display_algo_b)
        self.btn_best.clicked.connect(self.display_best_algo)
        self.word_input.returnPressed.connect(self.add_to_word_list)
        
        self.resize(self.win_w, self.win_h)
        self.center()

        self.setWindowTitle("Crossword Scratcher Optimizer")
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def clear_fields(self):

        self.letter_input.clear()
        self.word_input.clear()
        self.word_list.clear()
        self.letter_list.clear()

    def add_to_word_list(self):
        
        self.word_list.addItem(self.word_input.text())
        self.word_input.clear()

    def display_algo_a(self):

        current_board = Board(self.word_list.count(), int(self.letter_input.text()))

        word_array = []
        for i in range(self.word_list.count()):
            word_array.append(self.word_list.item(i).text())

        current_board.gui_input(word_array)

        current_board.optmize_char_count()

        self.letter_list.clear()
        self.letter_list.addItems(current_board.letters_occ)

    def display_algo_b(self):

        current_board = Board(self.word_list.count(), int(self.letter_input.text()))

        word_array = []
        for i in range(self.word_list.count()):
            word_array.append(self.word_list.item(i).text())

        current_board.gui_input(word_array)

        current_board.optimize_small_words()

        self.letter_list.clear()
        self.letter_list.addItems(current_board.letters_osw)

    def display_best_algo(self):

        current_board = Board(self.word_list.count(), int(self.letter_input.text()))

        word_array = []
        for i in range(self.word_list.count()):
            word_array.append(self.word_list.item(i).text())

        current_board.gui_input(word_array)

        current_board.optmize_char_count()
        current_board.optimize_small_words()

        self.letter_list.clear()
        self.letter_list.addItems(current_board.get_optimal_set()[0])



def main():
    
    app = QApplication(sys.argv)

    win = Window()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
