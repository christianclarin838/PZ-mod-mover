from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont

import sys
import os

icon_path = os.path.join(os.path.dirname(__file__), "..", "resources", "img", "icon.png")

class MainDisplay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PZ Mod Mover")
        self.setGeometry(700, 300 ,600, 400)
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        label = QLabel("PZ Mod Mover", self)
        label.setFont(QFont('Arial'))


def main():
    app = QApplication(sys.argv)
    window = MainDisplay()
    window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()