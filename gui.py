import sys

from PyQt6.QtWidgets import QApplication, QWidget

from main import Board

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()   


    def initUI(self):
        
        self.resize(250, 200)
        self.move(300, 300)

        self.setWindowTitle("Crossword Scratcher Optimizer")
        self.show()


def main():
    
    app = QApplication(sys.argv)

    win = Window()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
