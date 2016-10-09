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
        self.loadImages()

    def paint(self, painter, option, widget):
        # Only to indicate the area for the board
        painter.setBrush(QColor(Qt.cyan))
        painter.drawRect(Board.TOPLEFT_X, Board.TOPLEFT_Y,
                            Board.WIDTH, Board.HEIGHT)

    def boundingRect(self):
        return QRectF(Board.TOPLEFT_X, Board.TOPLEFT_Y,
                            Board.WIDTH, Board.HEIGHT)

    def loadImages(self):
        global BOARDIMG, REDDISK, BLACKDISK
        BOARDIMG = QImage("assets/4row_board.png").scaled(Board.CELLSIZE,
                                            Board.CELLSIZE, Qt.KeepAspectRatio)
        REDDISK = QImage("assets/4row_red.png").scaled(Board.CELLSIZE,
                                            Board.CELLSIZE, Qt.KeepAspectRatio)
        BLACKDISK = QImage("assets/4row_black.png").scaled(Board.CELLSIZE,
                                            Board.CELLSIZE, Qt.KeepAspectRatio)


class DropArea(QGraphicsObject):
    WIDTH = 400
    HEIGHT = 75
    TOPLEFT_X = Board.TOPLEFT_X
    TOPLEFT_Y = Board.TOPLEFT_Y - HEIGHT
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.dragOver = False

    def paint(self, painter, option, widget):
        # No need to display this area but for debug
        painter.setBrush(QColor(Qt.darkGreen))
        painter.drawRect(DropArea.TOPLEFT_X, DropArea.TOPLEFT_Y,
                        DropArea.WIDTH, DropArea.HEIGHT)

    def boundingRect(self):
        return QRectF(DropArea.TOPLEFT_X, DropArea.TOPLEFT_Y,
                        DropArea.WIDTH, DropArea.HEIGHT)

class Player(QGraphicsObject):
    def __init__(self):
        super().__init__()
        self.dropped = False

    def paint(self, painter, option, widget):
        # Player drag a red disk from here
        painter.drawImage(-275, 225, REDDISK)

    def boundingRect(self):
        return QRectF(-275, 225, REDDISK.width(), REDDISK.height())

