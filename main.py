import tkinter as tk 
import pygame


#This class creates a menu with 3 functions: Start, Help and Exit in Tkinter before the game
class Menu():
    def __init__(self):
        self.root = tk.Tk()
        gui = tk.Frame(self.root)
        gui.master.title("Sweet Race Menu")
        self.root.geometry("250x200")
        btn_exit = tk.Button(self.root, text="Exit", command=self.quit)
        btn_help = tk.Button(self.root, text="Help", command=self.help)
        btn_start = tk.Button(self.root, text="Start", command=self.start)
        btn_start.pack(pady=5)
        btn_help.pack(pady=5)
        btn_exit.pack(pady=5)
        
        self.root.mainloop()

    
    def start(self):
        pygame.font.init()
        from game.director import draw
        draw()
    def help(self):
        instructions = """
Press W to accelerate
Press S to reverse
Press A to turn left
Press D to turn right"""
        lb1 = tk.Label(self.root, text=instructions, justify="center")
        lb1.pack(pady=5)

    def quit(self):
        self.root.destroy()
        pygame.quit()
        
   


if __name__ == "__main__":
    Menu()
