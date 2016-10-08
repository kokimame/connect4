from PyQt5.QtWidgets import (QGraphicsObject)
from PyQt5.QtCore import (Qt, QRectF)
from PyQt5.QtGui import (QColor, QImage)


class Board(QGraphicsObject):
    ROW, COL = 8, 8
    WIDTH, HEIGHT = 400, 400
    TOPLEFT_X, TOPLEFT_Y = -200, -200
    CELLSIZE = 50

    def __init__(self):
        super().__init__()
        self.grid = [[0] * Board.ROW for _ in range(Board.COL)]

    def paint(self, painter, option, widget):
        # Only to indicate the area for the board
        painter.setBrush(QColor(Qt.cyan))
        painter.drawRect(Board.TOPLEFT_X, Board.TOPLEFT_Y,
                            Board.WIDTH, Board.HEIGHT)

    def boundingRect(self):
        return QRectF(Board.TOPLEFT_X, Board.TOPLEFT_Y,
                            Board.WIDTH, Board.HEIGHT)

