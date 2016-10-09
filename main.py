import sys

from PyQt5.QtWidgets import (QApplication, QGraphicsScene, QGraphicsView,
        QMainWindow, QGraphicsRectItem)
from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import (QColor)

from field import *

class GraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        QGraphicsView.__init__(self, parent=parent)
        self.setBackgroundBrush(QColor(125, 255, 125))

        board = Board()
        player = Player()
        computer = Computer(board)
        dropArea = DropArea(board, computer)
 
        scene = QGraphicsScene(self)
        scene.addItem(board)
        scene.addItem(dropArea)
        scene.addItem(player)
        self.setScene(scene)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle("Connect 4")

        view = GraphicsView()
        self.setCentralWidget(view)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
