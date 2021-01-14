import copy

class Grid:
    def __init__(self): # grid constructor, creates grid 20 tall, 10 wide
        self.arr = []
        for r in range(20):
            self.arr.append([])
            for c in range(10):
                self.arr[r].append([0, (0, 0, 0)]) #the tuple is for RGB colors and the int tells the code whether to draw the
                                                # square or not

    def get_color(self,rows,cols): # returns color at a specific coordinate on grid
        return self.arr[rows][cols][1]

    def get_bin(self,rows,cols): # returns bin at specified coordinates
        return self.arr[rows][cols][0]

    # changes color to specified color at coordinates given
    def set_color(self,rows,cols,color): # color must be a tuple of length 3
        self.arr[rows][cols][1] = color

    # changes bin based on num at specified coordinates
    def set_bin(self,rows,cols,num): # either 0 or 1
        self.arr[rows][cols][0] = num

    def get_arr(self): # returns array
        return self.arr

    def get_index(self,rows,cols): # returns index at specified coordinates
        return self.arr[rows][cols]

    # prints grid, for testing purposes
    def print_grid(self): #just to be able to visualize what is going on
        for i in self.arr:
            print(i)

    def grid_reset(self): # resets grid to be empty
        self.arr.clear()
        for r in range(20):
            self.arr.append([])
            for c in range(10):
                self.arr[r].append([0, (0, 0, 0)])



if __name__ == "__main__": # initializes grid
    grid1 = Grid()
    grid1.print_grid()