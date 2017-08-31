#!/usr/bin/python3.5
class App:
    def __init__(self, tk, surface):
        from tkinter import messagebox
        surface.minsize(width=300, height=350)
        surface.maxsize(width=300, height=350)#set height
        surface.title('X and O')
    def game_Buttons(self, tk, surface, playing):
        self.B1 = tk.Button(surface, text='', width=13, height=6, fg='white', command=playing.onclick_event_B1)# setting the command and font
        self.B2 = tk.Button(surface, text='', width=13, height=6, fg='white', command=playing.onclick_event_B2)# set them to a frame
        self.B3 = tk.Button(surface, text='', width=13, height=6, fg='white', command=playing.onclick_event_B3)
        self.B4 = tk.Button(surface, text='', width=13, height=6, fg='white', command=playing.onclick_event_B4)
        self.B5 = tk.Button(surface, text='', width=13, height=6, fg='white', command=playing.onclick_event_B5)
        self.B6 = tk.Button(surface, text='', width=13, height=6, fg='white', command=playing.onclick_event_B6)
        self.B7 = tk.Button(surface, text='', width=13, height=6, fg='white', command=playing.onclick_event_B7)
        self.B8 = tk.Button(surface, text='', width=13, height=6, fg='white', command=playing.onclick_event_B8)
        self.B9 = tk.Button(surface, text='', width=13, height=6, fg='white', command=playing.onclick_event_B9)
        #self.B1.config(fontsize='40')
        self.B1.grid(row=1, column=1)
        self.B2.grid(row=1, column=2)
        self.B3.grid(row=1, column=3)
        self.B4.grid(row=2, column=1)
        self.B5.grid(row=2, column=2)
        self.B6.grid(row=2, column=3)
        self.B7.grid(row=3, column=1)
        self.B8.grid(row=3, column=2)
        self.B9.grid(row=3, column=3)
    def chalange_computer(self, tk, surface, playing):
        self.chalange_B = tk.Button(surface, text='chalange!',width=13 ,height=3 , command=playing.compyter_event)#set width and height
        self.chalange_B.grid(row=4,column=1)
    def try_again(self, tk, surface, playing):
        self.restart = tk.Button(surface, text='try again!',width=13 ,height=3 , command=playing.restart)
        self.restart.grid(row=4,column=2)
    def winner_message(self, tk):
        tk.messagebox.showinfo('winner!', 'you win!!!')
    def loser_message(self, tk):
        tk.messagebox.showinfo('loser!', 'you lose!!!')
