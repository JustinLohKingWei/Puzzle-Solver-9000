
from typing import List


class h_node:
    def __init__(self, current):
        self.prev = []
        self.current = current
        self.down = []
        self.up = []
        self.left = []
        self.right = []

    def setDownMove(self, move):
        self.down = move

    def setUpMove(self, move):
        self.up = move

    def setLeftMove(self, move):
        self.left = move

    def setRightMove(self, move):
        self.right = move

    def setPrevMove(self, move):
        self.prev = move

    def gerPrevMove(self):
        return self.prev

    def getMoves(self):
        return [self.down, self.up, self.left, self.right]

    def __str__(self):
        return "Current:   "+str(self.current)+"\nDown:   "+str(self.down)+"\nUp:    "+str(self.up)+"\nLeft:     "+str(self.left)+"\nRight:   "+str(self.right)


class move_node:
    def __init__(self, current: List[str], prev):
        self.current = current
        self.prev = prev

    def getPrev(self):
        return self.prev

    def getCurrent(self):
        return self.current

        # and self.prev==__o.prev

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, move_node) and self.current == __o.current

    def __ne__(self, __o: object) -> bool:
        return not self == __o
