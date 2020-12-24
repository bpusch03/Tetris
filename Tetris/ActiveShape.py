

class ActiveShape():
    def __init__(self):
        self.coords = [[(0, 0), (0, 0, 0)], [(0, 0), (0, 0, 0)], [(0, 0), (0, 0, 0)], [(0, 0), (0, 0, 0)]]

    def shift_shape(self, vertical ,shift): # vertical - bool, shift - int (either 1 or -1)
        if vertical:                        #negative is up and positive is down
            for i in range(4):              # dont forget to put trys in the main so id doesn't shift out of bounds
                self.coords[i][0][1] = self.coords[i][0][1] + shift
        else:
            for i in range(4):
                self.coords[i][0][0] = self.coords[i][0][0] + shift


