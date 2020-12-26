import copy

class Grid:
    def __init__(self):
        rows = 20
        cols = 10
        self.arr = []
        for r in range(rows):
            self.arr.append([])
            for c in range(cols):
                self.arr[r].append([0,(0,0,0)])
        '''self.arr = [col[[0,(0,0,0)]].clone()*cols].clone()*rows #the tuple is for RGB colors and the int tells the code whether to draw the
                                             # square or not'''

    def get_color(self,rows,cols):
        return self.arr[rows][cols][1]

    def get_bin(self,rows,cols):
        return self.arr[rows][cols][0]

    def set_color(self,rows,cols,color): # color must be a tuple of length 3
        self.arr[rows][cols][1] = color

    def set_bin(self,rows,cols,num): # either 0 or 1
        self.arr[rows][cols][0] = num

    def get_arr(self):
        return self.arr

    def get_index(self,rows,cols):
        return self.arr[rows][cols]

    def print_grid(self): #just to be able to visualize what is going on
        for i in self.arr:
            print(i)


if __name__ == "__main__":
    grid1 = Grid()
    grid1.print_grid()