import threading
import math
from tkinter import *
from lib.board_pieces import *








class Main:
    def __init__(self):
        self.WIDTH = 500
        self.HEIGHT = 500
        # Height and width of canvas
        self.SIZE = [8, 8]
        self.GAME = "normal"
        self.main_window = Tk()
        self.canvas = Canvas(self.main_window, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()
        self.piece_list =[]
        self.piece_creation()

        self.start()
        self.update()
    def start(self):




        self.canvas.pack()
        self.main_window.mainloop()


    def update(self):
        self.canvas.delete(all)

        global main_window
        self.board.draw_squares()

        global timer
        timer = threading.Timer(3, self.update)
        timer.start()
        global piece_list
        for i in piece_list:
            i.label.destroy()
            i.draw()

    def piece_creation(self):

        knight_bl_1 = Knight(self,"black", 0)
        self.piece_list.append(knight_bl_1)
        knight_bl_2 = Knight(self,"black", 1)
        self.piece_list.append(knight_bl_2)
        for i in range(16):
            if i <= 7:
                pawn = Pawn(self,"white", i)
            else:
                pawn = Pawn(self,"black", i - 8)
            self.piece_list.append(pawn)








def next_turn():
    pass







#knight = Knight("black", 1)
#print(knight.position)
#knight.move(3, True)
#piece_list.append(knight)
#print(knight.position)






main = Main()


