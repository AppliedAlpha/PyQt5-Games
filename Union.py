import sys, random

from PyQt5.QtWidgets import QApplication, QWidget


class Union(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        self.setFixedSize(self.size())
        self.setWindowTitle('UNION!')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Union()
    sys.exit(app.exec_())
