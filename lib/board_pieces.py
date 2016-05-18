import math
from tkinter import *

class Board():
    def __init__(self, game):

        self.square_size = [ self.WIDTH / self.SIZE[0], self.HEIGHT / self.SIZE[1]]
        self.square_coords = []
        # so it takes up all of screen

        self.line_coordsX = []
        self.line_coordsY = []
        self.game = game

        if self.game == "normal":
            self.board_create()

    def board_create(self):

        for i in range(self.SIZE[0] * self.SIZE[1]):
            # uses total area

            self.square_coords.append([(i % self.SIZE[0]) * self.square_size[0],
                                       math.floor(i / self.SIZE[1]) * self.square_size[1]])

            if not (i % self.SIZE[0]) * self.square_size[0] in self.line_coordsX:
                # % makes it move down the line then math.floor will bring it over one  when % brings it back up
                self.line_coordsX.append((i % self.SIZE[0]) * self.square_size[0])

            if not math.floor(i / self.SIZE[1]) * self.square_size[1] in self.line_coordsY:
                self.line_coordsY.append(math.floor(i / self.SIZE[1]) * self.square_size[1])

                # draws lines that will form squares/rectangles

    def draw_squares(self):

        for coords in self.line_coordsX:
            self.canvas.create_line(coords, 0, coords, self.HEIGHT)

        for coords in self.line_coordsY:
            self.canvas.create_line(0, coords, self.WIDTH, coords)







        # Creates timer every time it is called for an infinite loop so I can draw stuff


class Pieces:
    def __init__(self, main, side, number):
        self.main = main
        self.alive = True
        self.number = number
        self.side = side

        self.main.piece_list.append(self)

    def capture_check(self, temp_position, real, has_range=False):

        if temp_position[0] > 8 or temp_position[0] < 0 or temp_position[1] < 0 or temp_position[1] > 8:
            return False
        else:
            if not self.move(self, temp_position):
                return False
                # checks if outside then if not it checks if it is open
            if real:
                self.capture(self, temp_position)
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
        piece_list = self.main.piece_list
        can_move_side = False

        for piece in piece_list:
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
                    possible_move_positions.append([i, False])

    def capture(self,moving_piece, cords):

        for piece in self.piece_list:
            if piece.position == cords:
                if piece.side != moving_piece.side:
                    piece.alive = False

    def piece_location_open(self,moving_piece, coords):

        for piece in self.piece_list:
            if piece.position == coords:
                if piece.side == moving_piece.side:
                    return False
        return True


    def draw(self):

        screen_cords = [int(self.position[0]), int(self.SIZE[1] - self.position[1])]
        print(self.position)
        self.label = Label(self.main_window, text=self.letter)

        draw_cords = [int(screen_cords[0] * (self.WIDTH / 8) - self.WIDTH / 16),
                      int(screen_cords[1] * self.HEIGHT / (self.SIZE[1]) - self.HEIGHT / 16)]
        self.label.pack()
        self.label.place(x=draw_cords[0], y=draw_cords[1])


class Knight(Pieces):
    def __init__(self, main, side, number):
        self.possible_moves_no_range = 8
        super().__init__(main,side, number)
        self.letter = "K"

        if number == 0:
            if side == "white":
                self.position = [7, 1]
            else:
                self.position = [7, 7]
        if number == 1:
            if side == "black":
                self.position = [2, 7]
            else:
                self.position = [2, 1]

        screen_cords = [int(self.position[0]), int(self.main.SIZE[1] / self.position[1])]
        # print(self.position)
        self.label = Label(self.main.main_window, text=self.letter)

        draw_cords = [int(screen_cords[0] * (self.main.WIDTH / 8) - self.main.WIDTH / 16),
                      int(screen_cords[1] * self.main.HEIGHT / (self.main.SIZE[1]) - self.main.HEIGHT / 16)]
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
        self.possible_range = [4, 8]
        self.letter = "B"
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

    def move(self, number_list, real):
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
    def __init__(self,main, side, number):
        # positions the pawn based on which one it is
        self.letter = "P"
        super().__init__(main,side, number)
        # it is able to do that special first move
        self.two_start_move_thing = True
        if self.side == "white":
            self.position = [number + 1, 6]
        if self.side == "black":
            self.position = [number + 1, 1]

        screen_cords = [int(self.position[0]), int(self.main.SIZE[1] / self.position[1])]

        self.label = Label(self.main.main_window, text=self.letter)

        draw_cords = [int(screen_cords[0] * (self.main.WIDTH / 8) - self.main.WIDTH / 16),
                      int(screen_cords[1] * self.main.HEIGHT / (self.main.SIZE[1]) - self.main.HEIGHT / 16)]
        self.label.pack()
        self.label.place(x=draw_cords[0], y=draw_cords[1])

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
        if self.capture_check(temp_position, real, True):
            if real:
                self.position = temp_position
            return True
        else:
            return False