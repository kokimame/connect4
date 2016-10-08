import sys

from PyQt5.QtWidgets import (QApplication, QGraphicsScene, QGraphicsView,
        QMainWindow, QGraphicsRectItem)
from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import (QColor)

class GraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        QGraphicsView.__init__(self, parent=parent)

        scene = QGraphicsScene(self)

        item = QGraphicsRectItem(-200, -200, 400, 400)
        scene.addItem(item)
        
        self.setScene(scene)

        self.setBackgroundBrush(QColor(125, 255, 125))

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
