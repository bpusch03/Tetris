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


#im probably going to want to adda number list to show the next shapes that are coming
class Game:
    def __init__(self):
        self.grid = Grid()
        self.activeShape = ActiveShape()
        self.next_shape_num = 0
        self.activeShape.create_shapes(random.randint(1, 7))
        self.create_nextShape()
        self.DISPLAY = pygame.display.set_mode((GAMEWIDTH+UIWIDTH, GAMEHEIGHT))
        pygame.display.set_caption("Tetris")
        self.DISPLAY.fill(BLACK)
        # i don't have a game surface Surface object, im drawing right onto the display
        self.label_suface = pygame.Surface((UIWIDTH, GAMEHEIGHT))
        self.score = 0

        self.LINES_CLEARED = 0         # this should be config but i had to make it an attribute of the game class
        self.level = 1
        self.SPEED = 1000
        self.GAME_TICK = pygame.USEREVENT + 1
        pygame.time.set_timer(self.GAME_TICK, self.SPEED)

    def draw_scoreboard(self):
        score_text = font.render("Score: {}".format(str(self.score)), True, BLACK)
        next_shape_text = font.render("Next Shape: ", True, BLACK)
        self.label_suface.fill(WHITE)
        self.label_suface.blit(score_text, (0, GAMEHEIGHT/2))  # how do I make this go in the center
        self.label_suface.blit(next_shape_text, (0, GAMEHEIGHT/3))
        next_shape_text_width = pygame.font.Font.size(font,"Next Shape: ")[0]
        self.draw_next_shape(self.next_shape_num, next_shape_text_width)
        self.DISPLAY.blit(self.label_suface, (GAMEWIDTH, 0))

    def draw_next_shape(self, shape_type, width):
        if shape_type ==1:
            image_surface = pygame.image.load('Tetris Pics/i-shape.png')
            self.label_suface.blit(image_surface, (width, GAMEHEIGHT/3))
        if shape_type ==2:
            image_surface = pygame.image.load('Tetris Pics/o-shape.png')
            self.label_suface.blit(image_surface, (width, GAMEHEIGHT/3))
        if shape_type ==3:
            image_surface = pygame.image.load('Tetris Pics/j-shape.png')
            self.label_suface.blit(image_surface, (width, GAMEHEIGHT/3))
        if shape_type ==4:
            image_surface = pygame.image.load('Tetris Pics/s-shape.png')
            self.label_suface.blit(image_surface, (width, GAMEHEIGHT/3))
        if shape_type ==5:
            image_surface = pygame.image.load('Tetris Pics/t-shape.png')
            self.label_suface.blit(image_surface, (width, GAMEHEIGHT/3))
        if shape_type ==6:
            image_surface = pygame.image.load('Tetris Pics/z-shape.png')
            self.label_suface.blit(image_surface, (width, GAMEHEIGHT/3))
        if shape_type ==7:
            image_surface = pygame.image.load('Tetris Pics/L-shape.png')
            self.label_suface.blit(image_surface, (width, GAMEHEIGHT/3))


    def update_score(self, num_rows):  # don't know how the score works yet
        if num_rows == 1:
            self.score = self.score + 40 * (self.level + 1)
        elif num_rows == 2:
            self.score = self.score + 100 * (self.level + 1)
        elif num_rows == 3:
            self.score = self.score + 300 * (self.level + 1)
        elif num_rows == 4:
            self.score = self.score + 1200 * (self.level + 1)

    def create_nextShape(self):
        self.next_shape_num = random.randint(1,7)
    def create_activeShape(self):
        self.activeShape = ActiveShape()
        self.activeShape.create_shapes(self.next_shape_num)
        self.create_nextShape()

    def draw_activeShape(self):
        for i in range(4):
            x = self.activeShape.get_coords(i)[0]*SQUAREWIDTH
            y = self.activeShape.get_coords(i)[1]*SQUAREHEIGHT
            color = self.activeShape.get_color(i)
            pygame.draw.rect(self.DISPLAY, color, [x+2, y+2, SQUAREWIDTH-4, SQUAREHEIGHT-4], 2) # it was giving me a parameter
                                                                                     # error here but I ignored it
                                #might need to mess around with these numbers a littdddle bit --> i added the offset because
                                # of the way the boarder mechanic works

    def draw_grid(self):
        for r in range(20):
            for c in range(10):
                x = c * SQUAREWIDTH
                y = r * SQUAREWIDTH
                if self.grid.get_bin(r,c) == 1:
                    color = self.grid.get_color(r,c)
                    pygame.draw.rect(self.DISPLAY, color, [x+2, y+2, SQUAREWIDTH-4, SQUAREHEIGHT-4], 2)

    def draw_helper_lines(self):
        x_values = []
        for i in range(4):
            x_values.append(self.activeShape.get_coords(i)[0])
        x_values.sort()
        x1 = x_values[0] * SQUAREWIDTH
        x2 = x_values[3] * SQUAREWIDTH + SQUAREWIDTH
        pygame.draw.line(self.DISPLAY, GREY, (x1, 0), (x1, GAMEHEIGHT))
        pygame.draw.line(self.DISPLAY, GREY, (x2, 0), (x2, GAMEHEIGHT))


    def shift_horizontal(self, left_or_right):
        if self.activeShape.check_shift_shape(left_or_right, self.grid):
            self.activeShape.shift_shape(left_or_right)

    #what the game does to move the shapes down every second
    def shift_down(self):
        self.activeShape.game_shift_shape_down()

    def rotate(self):
        self.activeShape.rotate_shape(self.grid)


    #user input --> shifts the active square all the way to the bottom
    def move_down(self):
        no_collision = True

        while no_collision:
            self.shift_down()
            if self.check_collision():
                break


    def check_collision(self):
        if self.check_collision_bottom_out_of_bounds() or self.check_collsion_bottom_static_squares():
            return True
        return False

    def check_collision_bottom_out_of_bounds(self):
        for i in range(4):
            y = self.activeShape.get_coords(i)[1]
            if y > 19:
                return True
        return False

    def check_collsion_bottom_static_squares(self):
        for i in range(4):
            row = self.activeShape.get_coords(i)[1]
            col = self.activeShape.get_coords(i)[0]
            if self.grid.get_bin(row, col) == 1:
                return True
        return False

    def paste_onto_grid(self):
        static_squares = self.activeShape.active_shape_one_up()
        color = self.activeShape.get_color(0)
        for i in range(4):
            row = static_squares[i][1]
            col = static_squares[i][0]
            self.grid.set_bin(row, col, 1)
            self.grid.set_color(row,col,color)

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



    def shift_static_down(self, list1):
        for i in list1:
            for r in range(i,0,-1):
                for c in range(10):
                    self.grid.set_bin(r,c,self.grid.get_bin(r-1,c))
                    self.grid.set_color(r,c,self.grid.get_color(r-1,c))

                for c1 in range(10):
                    self.grid.set_bin(0,c1,0)
                    self.grid.set_color(0,c1,(0, 0, 0))

    def increase_level_and_update_speed(self):
        if self.LINES_CLEARED > 10:
            self.level = self.level+1
            self.LINES_CLEARED = 0
        if self.level > 0 and self.level < 16:
            self.SPEED = int(f(self.level)*1000)
            pygame.time.set_timer(self.GAME_TICK, self.SPEED)



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
            self.label_suface.fill(WHITE)
            self.label_suface.blit(score_text, (0, GAMEHEIGHT / 2))  # how do I make this go in the center
            self.label_suface.blit(font.render("Game Over: ", True, BLACK), (0, 0))
            self.label_suface.blit(font.render("Press <Enter> to play again ", True, BLACK), (0, 40))
            self.DISPLAY.blit(self.label_suface, (GAMEWIDTH, 0))


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

if __name__ == "__main__":
    tetris = Game()
    tetris.run_game()
