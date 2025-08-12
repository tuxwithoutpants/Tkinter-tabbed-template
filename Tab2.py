import tkinter as tk                    
from tkinter import ttk

class Tab2(tk.Frame):
	def __init__(self, container):
		super().__init__()
		
		self.label = tk.Label(self, text="Tab 2 place holder")
		self.label.grid(column=1, row=1)
