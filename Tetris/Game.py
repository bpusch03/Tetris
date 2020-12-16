def __init__(self):
    rows, cols = (11, 11)
    self.Grid = [['0' for i in range(cols)] for j in range(rows)]
    for r in range(20):
        for c in range(10):
            self.changeValue(c, 0, str(c))


def changeValue(self, letter, num, string):
    self.Grid[num][letter] = string