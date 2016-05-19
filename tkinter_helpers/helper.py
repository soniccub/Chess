import tkinter as tk


class Tkinter:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)

    def start(self):
        self.canvas.pack()
        self.root.mainloop()

    def draw_line(self, pos0, pos1, **options):
        return self.canvas.create_line(pos0, pos1, **options)

    def draw_text(self, pos, **options):
        return self.canvas.create_text(pos, **options)
