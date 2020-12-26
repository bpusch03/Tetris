from Grid import Grid
from ActiveShape import ActiveShape
import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

SPEED = 3      00
GAME_TICK = pygame.USEREVENT +1
pygame.time.set_timer(GAME_TICK,SPEED)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Verdana", 60)

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
        self.create_activeShape()
        self.DISPLAY = pygame.display.set_mode((GAMEWIDTH+UIWIDTH, GAMEHEIGHT))
        pygame.display.set_caption("Tetris")
        self.DISPLAY.fill(BLACK)
        # i don't have a game surface Surface object, im drawing right onto the display
        self.label_suface = pygame.Surface((UIWIDTH, GAMEHEIGHT))
        self.score = font.render("Score: {}".format(str(0)), True, BLACK)

    def draw_scoreboard(self):  # also updates it
        self.update_score()
        self.label_suface.fill(WHITE)
        self.label_suface.blit(self.score, (0, GAMEHEIGHT/2))  # how do I make this go in the center
        self.DISPLAY.blit(self.label_suface, (GAMEWIDTH, 0))

    def update_score(self):  # don't know how the score works yet
        pass

    def create_activeShape(self):
        self.activeShape.create_shapes(random.randint(1, 7))

    def draw_activeShape(self):
        for i in range(4):
            x = self.activeShape.get_coords(i)[0]*SQUAREWIDTH
            y = self.activeShape.get_coords(i)[1]*SQUAREHEIGHT
            color = self.activeShape.get_color(i)
            pygame.draw.rect(self.DISPLAY, color, [x+2, y+2, SQUAREWIDTH-4, SQUAREHEIGHT-4], 2) # it was giving me a parameter
                                                                                     # error here but I ignored it
                                #might need to mess around with these numbers a little bit --> i added the offset because
                                # of the way the boarder mechanic works

    def draw_grid(self):
        for r in range(20):
            for c in range(10):
                x = c * SQUAREWIDTH
                y = r * SQUAREWIDTH
                if self.grid.get_bin(r,c) == 1:
                    color = self.grid.get_color(r,c)
                    pygame.draw.rect(self.DISPLAY, color, [x+2, y+2, SQUAREWIDTH-4, SQUAREHEIGHT-4], 2)

    def shift_horizontal(self, left_or_right):
        if self.activeShape.check_shift_shape(left_or_right):
            self.activeShape.shift_shape(left_or_right)

    #what the game does to move the shapes down every second
    def shift_down(self):
        self.activeShape.game_shift_shape_down()

    def rotate(self):
        self.activeShape.rotate_shape(self.grid)


    #user input --> shifts the active square all the way to the bottom
    def move_down(self):
        pass

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

    '''this method isn't actually necessary since it is the same as the collision method,
            however I think it makes it more clear. The only important thing is when you call it, which is 
            right after a new active shape object is created'''
    def check_game_over(self):
        return self.check_collsion_bottom_static_squares()


    def run_game(self):
        run = True
        pause_toggle = True   # this is just temporary --> PROBABLY CAUSES AN ERROR IN THE RESTART
        while run:
            if pause_toggle:
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
                    if event.type == GAME_TICK:
                        self.shift_down()
                if self.check_collision():
                    self.paste_onto_grid()
                    self.create_activeShape()
                    if self.check_game_over():
                        self.label_suface.blit(font.render("Game Over", True, BLACK), (0,0))
                        pause_toggle = False # stopped here --> this is all jank

                self.DISPLAY.fill(BLACK)
                self.draw_scoreboard()
                self.draw_activeShape()
                self.draw_grid()

                #self.create_activeShape()
                pygame.display.update()
                #clock.tick(FPS)



if __name__ == "__main__":
    tetris = Game()
    tetris.run_game()
