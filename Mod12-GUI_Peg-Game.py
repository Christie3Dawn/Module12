# Procedural approach
"""
from PyQt5 import QtWidgets
import sys   # This was not in the instructions

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Was sys was unused argument before import
    main_window = QtWidgets.QWidget()
    main_window.show()
    app.exec_()
"""

# Using object-oriented approach to code above (lines 3 - 10)

from PyQt5 import QtWidgets
import sys   # This was not in the instructions

# Define interface
class PegGameWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup()

    # Alternative to lines 42 - 61
    def setup(self):
        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle('Triangle Peg Game')
        self.setToolTip("Play the triangle peg game!")
        self.new_button = QtWidgets.QPushButton("Start New Game", self)
        self.new_button.move(20, 160)
        self.quit_button = QtWidgets.QPushButton("Quit", self)
        self.quit_button.move(150, 160)

        self.central_widget == QtWidgets.QMainWindow(self)
        self.new_button = StartNewGameBtn(self.central_widget)
        self.quit_button = QuitBtn(self.central_widget)
        self.setCentralWidget(self.central_widget)

        exit_action = QtWidgets.QAction('Exit', self)
        exit_action.triggered.connect(QtWidgets.qApp.quit)

        menu_bar - self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_action)

        self.show()


    def closeEvent(self, event):
        reply = QuitMessage().exec_()
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class QuitMessage(QtWidgets.QMessageBox):
    def __init__(self):
        QtWidgets.QMessageBox.__init__(self)
        self.Text("Do you really want to quit?")
        self.addButton(self.No)
        self.addButton(self.Yes)

class QuitBtn(QtWidgets.QPushButton):
    def __init__(self, parent):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setText("Quit")
        self.move(150, 160)

        self.clicked.connect(QtWidgets.qApp.quit)
        self.setToolTip("Close the triangle peg game.")

# This section was presented out of order and caused confusion
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Was sys was unused argument/not defined before import
    main_window = PegGameWindow()
    app.exec_()

"""       
    def setup(self):
        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle('Triangle Peg Game')
        self.setToolTip("Play the triangle peg game!")
        self.new_button = StartNewGameBtn(self)
        self.quit_button = QuitBtn(self)
        self.show()

# Make buttons
class StartNewGameBtn(QtWidgets.QPushButton):
    def __init__(self, parent):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setText("Start New Game")
        self.move(20, 160)

class QuitBtn(QtWidgets.QPushButton):
    def __init__(self, parent):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setText("Quit")
        self.move(150, 160)
"""
