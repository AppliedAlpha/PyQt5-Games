import sys
import UnionBlock  # Local
# from . import UnionBlock  # Production

# PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QApplication, QPushButton, QTableWidget, QHeaderView, \
    QAbstractItemView, QTableWidgetItem, QLineEdit


class Union(QWidget):
    pic_grid = QGridLayout()

    def __init__(self):
        super().__init__()
        self.initUI()
        # self.item_labels = [for ]

    def initUI(self):
        # Layout
        grid = QGridLayout()
        self.setLayout(grid)

        # Setting Picture Grid
        for r in range(3):
            for c in range(3):
                pic_label = QLabel(f'[{r}, {c}]')
                pic_label.setAlignment(Qt.AlignCenter)
                self.pic_grid.addWidget(pic_label, r, c)

        # Setting Button Grid
        button_grid = QGridLayout()

        # Setting Label
        title_label = QLabel('Title Here')
        union_list_label = QLabel('Union List Here')
        time_label = QLabel('Time Here')

        title_label.setAlignment(Qt.AlignCenter)
        union_list_label.setAlignment(Qt.AlignCenter)
        time_label.setAlignment(Qt.AlignCenter)

        # Setting Button
        how_to_button = QPushButton('How to play')

        # Setting Table
        union_list_table = QTableWidget(16, 1)
        union_list_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        union_list_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        union_list_table.horizontalHeader().hide()
        union_list_table.verticalHeader().hide()
        union_list_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for r in range(16):
            item = QTableWidgetItem(f'[{r}] 0, 0, 0')
            item.setTextAlignment(Qt.AlignCenter)
            union_list_table.setItem(r, 0, item)

        # Setting Message Line
        message = QLineEdit('Message Comes Here...')
        message.setReadOnly(True)

        # Setting Grid
        grid.addWidget(title_label, 0, 0)
        grid.addWidget(how_to_button, 0, 1)
        grid.addLayout(self.pic_grid, 1, 0)
        grid.addWidget(union_list_table, 1, 1)
        grid.addWidget(time_label, 2, 0)
        grid.addLayout(button_grid, 2, 1)
        grid.addWidget(message, 3, 0, 1, 2)

        grid.setColumnStretch(0, 2)
        grid.setColumnStretch(1, 1)

        # Resize and Show
        self.setFixedWidth(500)
        self.setFixedHeight(550)
        self.setFixedSize(self.size())
        self.setWindowTitle('UNION!')
        self.show()

    def setText(self, item, x):
        prev = self.pic_grid.itemAtPosition(x // 3, x % 3)
        prev.widget().setParent(None)

        text = f'[{x // 3}, {x % 3}]\n' + '\n'.join(item.values())
        pic_label = QLabel(text)
        pic_label.setAlignment(Qt.AlignCenter)
        self.pic_grid.addWidget(pic_label, x // 3, x % 3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Union()

    # Logic
    print('Testing Logic...')

    blocks = UnionBlock.generate_blocks()
    answers = UnionBlock.get_answers(blocks)

    while len(answers) > 15:
        blocks = UnionBlock.generate_blocks()
        answers = UnionBlock.get_answers(blocks)

    for idx in range(len(blocks)):
        main.setText(blocks[idx], idx)
        print(blocks[idx])

    print(answers)

    # Exit
    sys.exit(app.exec_())
