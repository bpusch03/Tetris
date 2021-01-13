from Grid import Grid
from ActiveShape import ActiveShape
import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()


#Speed function
f = lambda x: 1.24 - (.258* x) + (0.0188 * x**2) - ((4.69 * 10**-4) * x**3)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (38, 38, 38)

font = pygame.font.SysFont("Verdana", 20)

# these should be multiples of 10 and 20 respectivly (same multiples) --> just use common sense
GAMEWIDTH = 400
GAMEHEIGHT = 800
UIWIDTH = 300

#dont change these values
SQUAREWIDTH = GAMEWIDTH/10
SQUAREHEIGHT = GAMEHEIGHT/20


class Game:
    def __init__(self): # constructor for game class, initializes grid, active shape, speed, and scoring trackers
        self.grid = Grid()
        self.activeShape = ActiveShape()
        self.next_shape_num = 0
        self.activeShape.create_shapes(random.randint(1, 7))
        self.create_nextShape()
        self.DISPLAY = pygame.display.set_mode((GAMEWIDTH+UIWIDTH, GAMEHEIGHT))
        pygame.display.set_caption("Tetris")
        self.DISPLAY.fill(BLACK)
        # no game surface Surface object, instead drawing right onto the display
        self.label_surface = pygame.Surface((UIWIDTH, GAMEHEIGHT))
        self.score = 0
        self.LINES_CLEARED = 0
        self.level = 1
        self.SPEED = 1000
        self.GAME_TICK = pygame.USEREVENT + 1
        pygame.time.set_timer(self.GAME_TICK, self.SPEED)

    def draw_scoreboard(self): # draws scoreboard, includes text "Score:" and "Next shape:"
        score_text = font.render("Score: {}".format(str(self.score)), True, BLACK)
        next_shape_text = font.render("Next Shape: ", True, BLACK)
        self.label_surface.fill(WHITE)
        self.label_surface.blit(score_text, (105, GAMEHEIGHT/2 + 50))  # how do I make this go in the center
        self.label_surface.blit(next_shape_text, (95, GAMEHEIGHT/3 - 50))
        next_shape_text_width = pygame.font.Font.size(font,"Next Shape: ")[0]
        self.draw_next_shape(self.next_shape_num, next_shape_text_width)
        self.DISPLAY.blit(self.label_surface, (GAMEWIDTH, 0))

    def draw_next_shape(self, shape_type, width): # draws next shape outside of the grid to let player know what's coming
        if shape_type ==1:
            image_surface = pygame.image.load('Tetris Pics/i-shape.png')
            self.label_surface.blit(image_surface, (width, GAMEHEIGHT/3))
        if shape_type ==2:
            image_surface = pygame.image.load('Tetris Pics/o-shape.png')
            self.label_surface.blit(image_surface, (width, GAMEHEIGHT/3))
        if shape_type ==3:
            image_surface = pygame.image.load('Tetris Pics/j-shape.png')
            self.label_surface.blit(image_surface, (width, GAMEHEIGHT/3))
        if shape_type ==4:
            image_surface = pygame.image.load('Tetris Pics/s-shape.png')
            self.label_surface.blit(image_surface, (width, GAMEHEIGHT/3))
        if shape_type ==5:
            image_surface = pygame.image.load('Tetris Pics/t-shape.png')
            self.label_surface.blit(image_surface, (width, GAMEHEIGHT/3))
        if shape_type ==6:
            image_surface = pygame.image.load('Tetris Pics/z-shape.png')
            self.label_surface.blit(image_surface, (width, GAMEHEIGHT/3))
        if shape_type ==7:
            image_surface = pygame.image.load('Tetris Pics/L-shape.png')
            self.label_surface.blit(image_surface, (width, GAMEHEIGHT/3))


    def update_score(self, num_rows):  # updates score every time the score changes to make scoreboard accurate
        if num_rows == 1:
            self.score = self.score + 40 * (self.level + 1)
        elif num_rows == 2:
            self.score = self.score + 100 * (self.level + 1)
        elif num_rows == 3:
            self.score = self.score + 300 * (self.level + 1)
        elif num_rows == 4:
            self.score = self.score + 1200 * (self.level + 1)

    def create_nextShape(self): # generates random number from 1 to 7 to create the next shape
        self.next_shape_num = random.randint(1, 7)

    def create_activeShape(self): # creates the active shape based on what was the next shape
        self.activeShape = ActiveShape()
        self.activeShape.create_shapes(self.next_shape_num)
        self.create_nextShape()

    def draw_activeShape(self): # draws the active shape at the top of the board
        for i in range(4):
            x = self.activeShape.get_coords(i)[0]*SQUAREWIDTH
            y = self.activeShape.get_coords(i)[1]*SQUAREHEIGHT
            color = self.activeShape.get_color(i)
            pygame.draw.rect(self.DISPLAY, color, [x+2, y+2, SQUAREWIDTH-4, SQUAREHEIGHT-4], 2)


    def draw_grid(self): # draws grid
        for r in range(20):
            for c in range(10):
                x = c * SQUAREWIDTH
                y = r * SQUAREWIDTH
                if self.grid.get_bin(r,c) == 1:
                    color = self.grid.get_color(r,c)
                    pygame.draw.rect(self.DISPLAY, color, [x+2, y+2, SQUAREWIDTH-4, SQUAREHEIGHT-4], 2)

    def draw_helper_lines(self): # draws vertical grey lines to guide the active shape
        x_values = []
        for i in range(4):
            x_values.append(self.activeShape.get_coords(i)[0])
        x_values.sort()
        x1 = x_values[0] * SQUAREWIDTH
        x2 = x_values[3] * SQUAREWIDTH + SQUAREWIDTH
        pygame.draw.line(self.DISPLAY, GREY, (x1, 0), (x1, GAMEHEIGHT))
        pygame.draw.line(self.DISPLAY, GREY, (x2, 0), (x2, GAMEHEIGHT))

    # shifts the active shape left or right by one, depending on left or right
    def shift_horizontal(self, left_or_right):
        if self.activeShape.check_shift_shape(left_or_right, self.grid):
            self.activeShape.shift_shape(left_or_right)

    # what the game does to move the shapes down every second
    def shift_down(self):
        self.activeShape.game_shift_shape_down()

    def rotate(self): # rotates active shape
        self.activeShape.rotate_shape(self.grid)


    #user input --> shifts the active square all the way to the bottom
    def move_down(self):
        no_collision = True

        while no_collision:
            self.shift_down()
            if self.check_collision():
                break

    # returns true if there is a collision, false if no collision when moving square to bottom
    def check_collision(self):
        if self.check_collision_bottom_out_of_bounds() or self.check_collsion_bottom_static_squares():
            return True
        return False

    def check_collision_bottom_out_of_bounds(self): # checks active shape to see if it travels out of the grid
        for i in range(4):
            y = self.activeShape.get_coords(i)[1]
            if y > 19:
                return True
        return False

    # checks active shape to see if it will collide with any static shapes
    def check_collsion_bottom_static_squares(self):
        for i in range(4):
            row = self.activeShape.get_coords(i)[1]
            col = self.activeShape.get_coords(i)[0]
            if self.grid.get_bin(row, col) == 1:
                return True
        return False

    def paste_onto_grid(self): # copies the active shape onto the grid as a static shape
        static_squares = self.activeShape.active_shape_one_up()
        color = self.activeShape.get_color(0)
        for i in range(4):
            row = static_squares[i][1]
            col = static_squares[i][0]
            self.grid.set_bin(row, col, 1)
            self.grid.set_color(row,col,color)

    # checks all rows to see if any are full, if full removes them, brings static shapes above that row down,
    # updates score and updates speed
    def row_clear(self):
        row = []
        for r in range(20):
            clear = True
            for c in range(10):
                if self.grid.get_bin(r,c) == 0:
                    clear = False

            if clear:
                row.append(r)

        self.shift_static_down(row)

        self.LINES_CLEARED = self.LINES_CLEARED + len(row)
        self.increase_level_and_update_speed()

        self.update_score(len(row))


    # shift static shapes down when a row is cleared
    def shift_static_down(self, list1):
        for i in list1:
            for r in range(i,0,-1):
                for c in range(10):
                    self.grid.set_bin(r,c,self.grid.get_bin(r-1,c))
                    self.grid.set_color(r,c,self.grid.get_color(r-1,c))

                for c1 in range(10):
                    self.grid.set_bin(0,c1,0)
                    self.grid.set_color(0,c1,(0, 0, 0))

    # depending on the number of lines cleared, calculate level, determine speed
    def increase_level_and_update_speed(self):
        if self.LINES_CLEARED > 10:
            self.level = self.level+1
            self.LINES_CLEARED = 0
        if self.level > 0 and self.level < 16:
            self.SPEED = int(f(self.level)*1000)
            pygame.time.set_timer(self.GAME_TICK, self.SPEED)


    # runs game
    def run_game(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.shift_horizontal(-1)
                    if event.key == pygame.K_d:
                        self.shift_horizontal(1)
                    if event.key == pygame.K_w:
                        self.rotate()
                    if event.key == pygame.K_s:
                        self.move_down()
                if event.type == self.GAME_TICK:
                    self.shift_down()
            if self.check_collision():
                self.paste_onto_grid()
                self.row_clear()
                self.create_activeShape()
                if self.check_collision():
                    run = False

            self.DISPLAY.fill(BLACK)
            self.draw_scoreboard()
            self.draw_activeShape()
            self.draw_grid()
            self.draw_helper_lines()

            # self.create_activeShape()
            pygame.display.update()
            # clock.tick(FPS)

        self.game_over()

    # prints game over and gives option to reset game and play again
    def game_over(self):
        reset = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        reset = True

            self.DISPLAY.fill(BLACK)

            score_text = font.render("Score: {}".format(str(self.score)), True, BLACK)
            self.label_surface.fill(WHITE)
            self.label_surface.blit(score_text, (0, GAMEHEIGHT / 2))  # how do I make this go in the center
            self.label_surface.blit(font.render("Game Over: ", True, BLACK), (0, 0))
            self.label_surface.blit(font.render("Press <Enter> to play again ", True, BLACK), (0, 40))
            self.DISPLAY.blit(self.label_surface, (GAMEWIDTH, 0))


            self.draw_grid()
            pygame.display.update()
            if reset:
                break

        if reset:
            self.reset_game()
            self.run_game()

    def reset_game(self):
        self.grid.grid_reset()
        self.create_activeShape()
        self.score = 0
        self.LINES_CLEARED = 0
        self.level = 1
        self.SPEED = 1000

if __name__ == "__main__": # initializes game
    tetris = Game()
    tetris.run_game()
