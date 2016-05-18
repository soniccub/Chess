import threading
import math
from tkinter import *

WIDTH = 500
HEIGHT = 500
# Height and width of canvas
SIZE = [8, 8]
GAME = "normal"
main_window = Tk()
label_pieces = []
canvas = Canvas(main_window, width=WIDTH, height=HEIGHT)
# using Tkinter to make a window
canvas.pack()


piece_list = []


class Board:

    def __init__(self,game):

        self.square_size = [WIDTH / SIZE[0], HEIGHT / SIZE[1]]
        self.square_coords = []
        # so it takes up all of screen

        self.line_coordsX = []
        self.line_coordsY = []
        self.game = game
        
        if self.game == "normal":

            self.board_create()
        
    def board_create(self):

        for i in range(SIZE[0]*SIZE[1]):
            # uses total area 
            
            self.square_coords.append([(i % SIZE[0]) * self.square_size[0], 
                                       math.floor(i / SIZE[1]) * self.square_size[1]])
                        
            if not (i % SIZE[0]) * self.square_size[0] in self.line_coordsX:
                # % makes it move down the line then math.floor will bring it over one  when % brings it back up
                self.line_coordsX.append((i % SIZE[0]) * self.square_size[0])

            if not math.floor(i / SIZE[1]) * self.square_size[1] in self.line_coordsY:
               
                self.line_coordsY.append(math.floor(i / SIZE[1]) * self.square_size[1])
                
            # draws lines that will form squares/rectangles   
    def draw_squares(self):
        
        for coords in self.line_coordsX:
            
            canvas.create_line(coords, 0, coords, HEIGHT)

        for coords in self.line_coordsY:
        
            canvas.create_line(0, coords, WIDTH, coords)
        

def draw_loop():
    canvas.delete(all)

    global main_window
    board.draw_squares()

    global timer
    timer = threading.Timer(1, draw_loop)
    timer.start()
    global piece_list
    for i in piece_list:
        i.label.destroy()
        i.draw()

    canvas.pack()


    # Creates timer every time it is called for an infinite loop so I can draw stuff


class Pieces:
    def __init__(self, side, number):
        self.alive = True
        self.number = number
        self.side = side
        global piece_list
        piece_list.append(self)

    def capture_check(self, temp_position, real,has_range=False):

        if temp_position[0] > 8 or temp_position[0] < 0 or temp_position[1] < 0 or temp_position[1] > 8:
            return False
        else:
            if not piece_location_open(self, temp_position):
                return False
                # checks if outside then if not it checks if it is open
            if real:
                capture(self, temp_position)
            return True

    def possible_moves_no_range(self):
        possible_moves = 0
        possible_positions = []
        for move in range(self.possible_moves_no_range[0]):
            if move(move, False):
                possible_moves += 1
                possible_positions.append(move)
        return possible_moves, possible_positions
    
    def possible_moves_range(self):
        possible_positions = []
        possible_moves = 0
        for i in range(self.possible_range[0]):
            possible_positions = []
            in_range = True
            for ii in range(self.possible_range[1]):
                if self.move([i, ii], False) and in_range:
                    possible_moves += 1
                    possible_positions.append([i, ii])
                else:
                    in_range = False
        return possible_moves, possible_positions

    def pawn_range(self):
        global piece_list
        self.piece_list = piece_list
        can_move_side = False

        for piece in self.piece_list:
            if piece.position == self.position:
                if piece.side != self.side:
                    can_move_side = True

        can_move_side = True

        possible_moves = 0
        possible_move_positions = []
        for i in range(2):
            if self.move([False, i], False):
                possible_moves += 1
                possible_move_positions.append([False, i])
        if can_move_side:
            for i in range(2):
                if self.move[i, False]:
                    possible_moves += 1
                    possible_move_positions.append([i,False])

    def draw(self):

        screen_cords = [int(self.position[0]), int(SIZE[1]-self.position[1])]
        print(self.position)
        self.label = Label(main_window, text=self.letter)

        draw_cords = [int(screen_cords[0] * (WIDTH/8)-WIDTH/16), int(screen_cords[1] * HEIGHT/(SIZE[1])-HEIGHT/16)]
        self.label.pack()
        self.label.place(x=draw_cords[0],y=draw_cords[1])






class Knight(Pieces):
    def __init__(self, side, number):
        self.possible_moves_no_range = 8
        super().__init__(side, number)
        self.letter = "K"
        label_pieces.append(Label(main_window,text=self.letter))
        if number == 0:
            if side == "white":
                self.position = [2, 1]
            else:
                self.position = [6, 1]
        if number == 1:
            if side == "black":
                self.position = [2, 8]
            else:
                self.position = [6, 8]

        screen_cords = [int(self.position[0]), int(SIZE[1] / self.position[1])]
        print(self.position)
        self.label = Label(main_window, text=self.letter)

        draw_cords = [int(screen_cords[0] * (WIDTH / 8) - WIDTH / 16), int(screen_cords[1] * HEIGHT / (SIZE[1]) - HEIGHT / 16)]
        self.label.pack()
        self.label.place(x=draw_cords[0], y=draw_cords[1])

        # sets position based on side given and a number given
        # leaves it open to new positions if I want to make the other game
    def move(self, number, real):

        self.temp_position = list(self.position)
        if number == 0:
            self.temp_position[0] += 1
            self.temp_position[1] += 3
            # moves it up and right
        if number == 2:
            self.temp_position[0] += -1
            self.temp_position[1] += 3
            # moves it up and left
        if number == 3:
            self.temp_position[0] += 1
            self.temp_position[1] += -3
            # moves it down and right

        if number == 4:
            self.temp_position[0] += -1
            self.temp_position[1] += -3
            # moves it down and left
# ########################################################################
# These are right or left three opposed to up or down 3
        if number == 5:
            self.temp_position[0] += 3
            self.temp_position[1] += 1
            # moves it right and up
        if number == 6:
            self.temp_position[0] += -3
            self.temp_position[1] += 1
            # moves it left and up

        if number == 7:
            self.temp_position[0] += 3
            self.temp_position[1] += -1
            # moves it right and down
            
        if number == 8:
            self.temp_position[0] += -3
            self.temp_position[1] += -1
            # moves it left and down

        if self.capture_check(self.temp_position, real):
            if real:
                self.position = self.temp_position
            return True
        else:
            return False
        # calls the function to see if it captures (or can't move somewhere)


class Bishop(Pieces):
    def __init__(self, side, number):
        super().__init__(side, number)
        self.possible_range = [4,8]
        self.letter = "B"
        label_pieces.append(Label(main_window, text=self.letter))
        if number == 0:
            if side == "white":
                self.position = [3, 1]
            else:
                self.position = [5, 1]
        if number == 1:
            if side == "black":
                self.position = [3, 8]
            else:
                self.position = [5, 8]

    def move(self, number_list,real):
        temp_position = list(self.position)

        if number_list[0] == 0:
            temp_position[0] += number_list
            temp_position[1] += number_list
            # Up and to the right

        if number_list[0] == 1:
            temp_position[0] -= number_list
            temp_position[1] += number_list
            # Up and to the left

        if number_list[0] == 2:
            temp_position[0] -= number_list
            temp_position[1] -= number_list
            # down and to the left
        if number_list[0] == 3:
            temp_position[0] += number_list
            temp_position[1] -= number_list
            # down and to the right

        if self.capture_check(temp_position, real):
            if real:
                self.position = temp_position
            return True
        else:
            return False


class Pawn(Pieces):
    def __init__(self, side, number):
        # positions the pawn based on which one it is
        self.letter = "P"
        super().__init__(side, number)
        # it is able to do that special first move
        self.two_start_move_thing = True
        if self.side == "white":
            self.position = [number+1, 2]
        if self.side == "black":
            self.position = [number+1, 7]
        label_pieces.append(Label(main_window, text=self.letter))

    def move(self, number_list, real=False):
        temp_position = list(self.position)

        if self.side == "white":
            if number_list[1] == 0:

                temp_position[1] += 1

            if number_list == 1 and self.two_start_move_thing:
                temp_position += 2

        if self.side == "black":
            if number_list[1] == 0:
                temp_position[1] += -1

            if number_list[1] == 1 and self.two_start_move_thing:
                temp_position[1] += -2

        if number_list[0] == 1:
            if self.side == "black":
                temp_position += [-1, -1]
            else:
                temp_position += [1, 1]

        if number_list[0] == 0:
            if self.side == "white":
                temp_position += [-1, 1]
            else:
                temp_position += [1, -1]

        if real:
            self.two_start_move_thing = False
        if self.capture_check(temp_position, real,True):
            if real:
                self.position = temp_position
            return True
        else:
            return False


def piece_location_open(moving_piece, coords):
    
    for peice in piece_list:
        if peice.position == coords:
            if peice.side == moving_piece.side:
                return False
    return True





def capture(moving_piece, cords):
    global piece_list

    for piece in piece_list:
        if piece.position == cords:
            if piece.side != moving_piece.side:
                piece.alive = False


def next_turn():
    pass


def pieces(game):
    if game == "regular":

        knight_bl_1 = Knight("black",1)
        piece_list.append(knight_bl_1)
        knight_bl_2 = Knight("black",2)
        piece_list.append(knight_bl_2)





knight = Knight("black", 1)
print(knight.position)
knight.move(3, True)
piece_list.append(knight)
print(knight.position)


board = Board(GAME)


draw_loop()

main_window.geometry()



canvas.pack()
main_window.mainloop()