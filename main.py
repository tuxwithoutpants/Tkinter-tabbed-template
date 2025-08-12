import tkinter as tk                    
from tkinter import ttk

from Tab1 import *
from Tab2 import *

class MainApp(tk.Tk):
	def __init__(self):
		super().__init__()
		
		self.title("Tkinter tabbed application template")
		self.geometry('640x480')

		self.notebook = ttk.Notebook(self)
		
		self.TabA = Tab1(self.notebook)
		self.TabB = Tab2(self.notebook)

		self.notebook.add(self.TabA, text='Tab One')
		self.notebook.add(self.TabB, text='Tab Two')

		self.notebook.pack(expand=True, fill='both')

if __name__ == '__main__':
	app = MainApp()
	app.mainloop()
