import random

from PyQt5.QtWidgets import (QGraphicsObject, QApplication)
from PyQt5.QtCore import (Qt, QRectF, QLineF, QMimeData, QPoint)
from PyQt5.QtGui import (QColor, QImage, QDrag, QPixmap)


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

        for i in range(Board.ROW):
            for j in range(Board.COL):
                if self.grid[i][j] == 1:
                    painter.drawImage(j*Board.CELLSIZE + Board.TOPLEFT_X,
                                  i*Board.CELLSIZE + Board.TOPLEFT_Y, REDDISK)
                elif self.grid[i][j] == 2:
                    painter.drawImage(j*Board.CELLSIZE + Board.TOPLEFT_X,
                                  i*Board.CELLSIZE + Board.TOPLEFT_Y, BLACKDISK)
                # Paint solid image for the grid of the board
                painter.drawImage(j*Board.CELLSIZE + Board.TOPLEFT_X,
                                  i*Board.CELLSIZE + Board.TOPLEFT_Y, BOARDIMG)

    def updateGrid(self, col, row, disk):
        self.grid[row][col] = disk
        self.update()

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
    def __init__(self, board, computer):
        super().__init__()
        self.setAcceptDrops(True)
        self.board = board
        self.computer = computer

    def dropEvent(self, event):
        col, row = self.getCellToDrop(event.pos().x(), event.pos().y())
        self.board.updateGrid(col, row, 1)  # The last argument is a flag for Player

        self.setAcceptDrops(False)
        self.computer.putDisk()
        self.setAcceptDrops(True)
        
    def getCellToDrop(self, mouseX, mouseY):
        currentCol = int((mouseX + 200) // Board.CELLSIZE)
        return currentCol, self.getEmptyRow(currentCol)

    def getEmptyRow(self, col):
        for i in range(Board.ROW-1, -1, -1):
            if self.board.grid[i][col] == 0:
                return i
        return -1

    def paint(self, painter, option, widget):
        # No need to display this area but for debug
        painter.setBrush(QColor(Qt.darkGreen))
        painter.drawRect(DropArea.TOPLEFT_X, DropArea.TOPLEFT_Y,
                        DropArea.WIDTH, DropArea.HEIGHT)

    def boundingRect(self):
        return QRectF(DropArea.TOPLEFT_X, DropArea.TOPLEFT_Y,
                        DropArea.WIDTH, DropArea.HEIGHT)

class Computer:
    def __init__(self, board):
        self.board = board

    def putDisk(self):
        # Show all cells where the computer can put a disk
        print(self.getAllValidCells())
        validCells = self.getAllValidCells()
        num = random.randint(0, len(validCells))
        self.board.updateGrid(validCells[num][0], validCells[num][1], 2)


    def getAllValidCells(self):
        validCells = []
        for j in range(Board.COL):
            for i in range(Board.ROW-1, -1, -1):
                if self.board.grid[i][j] == 0:
                    validCells.append([j, i]) # [col, row]
                    break
        return validCells

class Player(QGraphicsObject):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):
        self.setCursor(Qt.ClosedHandCursor)

    def mouseMoveEvent(self, event):
        if QLineF(event.screenPos(),
                event.buttonDownScreenPos(Qt.LeftButton)).length() < \
                        QApplication.startDragDistance():
            return

        drag = QDrag(event.widget())
        mime = QMimeData()
        drag.setMimeData(mime)

        mime.setImageData(REDDISK)
        dragImg = REDDISK.scaled(40, 40, Qt.KeepAspectRatio)
        drag.setPixmap(QPixmap.fromImage(dragImg))
        drag.setHotSpot(QPoint(dragImg.width() / 2, dragImg.height()/ 2))

        drag.exec()
        self.setCursor(Qt.OpenHandCursor)
        
    def mouseReleasedEvent(self, event):
        self.setCursor(Qt.OpenHandCursor)

    def paint(self, painter, option, widget):
        # Player drag a red disk from here
        painter.drawImage(-275, 225, REDDISK)

    def boundingRect(self):
        return QRectF(-275, 225, REDDISK.width(), REDDISK.height())

