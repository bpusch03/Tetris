class Grid:
    def __init__(self):
        rows = 20
        cols = 10
        self.arr = [[[0,(0,0,0)]]*cols]*rows #the tuple is for RGB colors and the int tells the code whether to draw the
                                             # square or not

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
    print(grid1.get_color(2,5))