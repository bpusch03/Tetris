
TURQUOISE = (64, 224, 208)  # --> for the I block
YELLOW = (204, 204, 0)      # --> for the O block
BLUE = (65, 105, 225)       # --> for the J block
GREEN = (50, 205, 50)       # --> for the S-block
PURPLE = (75, 0, 130)       # --> for the T-block
RED = (255, 0, 0)           # --> for the Z-block
ORANGE = (255, 140, 0)      # --> for the L-block

class ActiveShape():
    def __init__(self): # constructor for active shape, contains coordinates, center of rotation
        self.coords = [[[0, 0], (0, 0, 0)], [[0, 0], (0, 0, 0)], [[0, 0], (0, 0, 0)], [[0, 0], (0, 0, 0)]]
        self.center_of_rotation = [0,0] # using the nintendo rotation system, kind of --> not really
        self.identifier = ''
    def get_coords(self, index): # returns coordinates of first tile
        return self.coords[index][0]

    def get_color(self, index): # returns color in rgb format
        return self.coords[index][1]

    def clone_coords(self): # returns a copy of self's coordinates
        cloned_list = [1, 2, 3, 4]
        for i in range(4):
            cloned_list[i] = self.get_coords(i)[:]
        return cloned_list

    # returns true if the intended shift is valid,  false otherwise
    def check_shift_shape(self, shift, grid):
        coords_test = self.clone_coords()

        for i in range(4):
            coords_test[i][0] = coords_test[i][0] + shift
            if coords_test[i][0] > 9 or coords_test[i][0] < 0 or grid.get_bin(coords_test[i][1],coords_test[i][0]) == 1:
                del coords_test
                return False

        return True

    def game_shift_shape_down(self): # shifts all of self's coordinates down by one
        for i in range(4):
            self.coords[i][0][1] = self.coords[i][0][1]+1
        self.center_of_rotation[1] = self.center_of_rotation[1]+1

    def active_shape_one_up(self): # shifts all of self's coordinates up by one
        shifted_shape = self.clone_coords()
        for i in range(4):
            shifted_shape[i][1] = shifted_shape[i][1] - 1
        return shifted_shape
        pass

    # shifts coordinates by 1, direction depends on value of shift
    def shift_shape(self, shift): # shift - int (either 1 or -1)
        for i in range(4):
            self.coords[i][0][0] = self.coords[i][0][0] + shift
        self.center_of_rotation[0] = self.center_of_rotation[0]+ shift
        #print(self.center_of_rotation)

    # rotates the shape
    def rotate_shape(self,grid): #parameter is grid object
        rotation_coords = [[0,0], [0,0], [0,0], [0,0]]
        rotation_matrix = [0,-1,1,0] # not really a matrix, going top row then bottom row
        for i in range(4):
            rotation_coords[i][0] = self.coords[i][0][0]-self.center_of_rotation[0]
            rotation_coords[i][1] = self.coords[i][0][1] - self.center_of_rotation[1]
        if self.identifier == 'O':
            return
        elif self.identifier == 'I':
            vertical = False
            for i in range(4):
                if rotation_coords[i][1] == 0:
                    vertical = True

            if vertical:
                rotation_coords = [[0, 2], [1, 2], [2, 2], [3, 2]]
            else:
                rotation_coords = [[2, 0], [2, 1], [2, 2], [2, 3]]
        else:
            for i in range(4):
                rotation_coords[i] = [rotation_coords[i][1]*rotation_matrix[1], rotation_coords[i][0]*rotation_matrix[2]]
        inbounds = True
        for i in range(4):
            x = rotation_coords[i][0] + self.center_of_rotation[0]
            y = rotation_coords[i][1] + self.center_of_rotation[1]
            if x > 9 or x < 0 or y > 19 or y < 0:
                inbounds = False
            try:
                if grid.get_bin(y,x) == 1:
                    inbounds = False
            except:
                inbounds = False
                print("error triggered")

        if inbounds:
            for i in range(4):
                x = rotation_coords[i][0] + self.center_of_rotation[0]
                y = rotation_coords[i][1] + self.center_of_rotation[1]
                self.coords[i][0] = [x,y]

    # creates a specific shape based on num
    # 1 = I block
    # 2 = O block
    # 3 = J block
    # 4 = S block
    # 5 = T block
    # 6 = Z block
    # 7 = L block
    def create_shapes(self, num): #num has to be between 1-7 to create a random shape
        if num == 1:
            self.identifier = 'I'
            self.center_of_rotation = [3, 0]
            self.coords = [[[5, 0], TURQUOISE], [[5, 1], TURQUOISE], [[5, 2], TURQUOISE], [[5, 3], TURQUOISE]]
        elif num ==2:
            self.identifier = 'O'
            self.center_of_rotation = [0, 0] # doesn't have a center of rotation because it doesn't rotate
            self.coords = [[[4, 0], YELLOW], [[5, 0], YELLOW], [[4, 1], YELLOW], [[5, 1], YELLOW]]
        elif num ==3:
            self.identifier = 'J'
            self.center_of_rotation = [5, 1]
            self.coords = [[[5, 0], BLUE], [[5, 1], BLUE], [[5, 2], BLUE], [[4, 2], BLUE]]
        elif num ==4:
            self.identifier = 'S'
            self.center_of_rotation = [5, 0]
            self.coords = [[[6, 0], GREEN], [[5, 0], GREEN], [[5, 1], GREEN], [[4, 1], GREEN]]
        elif num == 5:
            self.identifier = 'T'
            self.center_of_rotation = [4, 1]
            self.coords = [[[4, 0], PURPLE], [[4, 1], PURPLE], [[5, 1], PURPLE], [[4, 2], PURPLE]]
        elif num == 6:
            self.identifier = 'Z'
            self.center_of_rotation = [4, 0]
            self.coords = [[[3, 0], RED], [[4, 0], RED], [[4, 1], RED], [[5, 1], RED]]
        elif num == 7:
            self.identifier = 'L'
            self.center_of_rotation = [4, 1]
            self.coords = [[[4, 0], ORANGE], [[4, 1], ORANGE], [[4, 2], ORANGE], [[5, 2], ORANGE]]

if __name__ == "__main__": # initializes active shape
    a = ActiveShape()
    cloned = a.clone_coords()
    print(cloned)
    print(a.active_shape_one_up())