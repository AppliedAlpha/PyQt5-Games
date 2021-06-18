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
    # app = QApplication(sys.argv)
    # main = Union()
    # sys.exit(app.exec_())

    # Logic
    print('Testing Logic ...')

    color = {"red": (255, 0, 0), "yellow": (255, 255, 0), "blue": (0, 0, 255)}
    background = {"white": (255, 255, 255), "gray": (127, 127, 127), "black": (0, 0, 0)}
    shape = ["circle", "triangle", "square"]

    for _ in range(9):
        block = {
            "color": random.choice(list(color.keys())),
            "background": random.choice(list(background.keys())),
            "shape": random.choice(shape)
        }
        print(f'#{_ + 1}: {list(block.values())}')
