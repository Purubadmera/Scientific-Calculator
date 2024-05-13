import tkinter as tk
from tkinter import ttk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        
        self.display = ttk.Entry(master, font=('Arial', 20), justify='right')
        self.display.grid(row=0, column=0, columnspan=5, sticky="ew")
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('π', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('sqrt', 5, 3), ('log', 5, 4)
        ]
        
        for (text, row, col) in buttons:
            ttk.Button(master, text=text, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, sticky="nsew")
        
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        
    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == 'C':
            self.display.delete(0, tk.END)
        elif char == 'π':
            self.display.insert(tk.END, math.pi)
        elif char == 'sin':
            self.display.insert(tk.END, math.sin(float(self.display.get())))
        elif char == 'cos':
            self.display.insert(tk.END, math.cos(float(self.display.get())))
        elif char == 'tan':
            self.display.insert(tk.END, math.tan(float(self.display.get())))
        elif char == 'sqrt':
            self.display.insert(tk.END, math.sqrt(float(self.display.get())))
        elif char == 'log':
            self.display.insert(tk.END, math.log(float(self.display.get())))

def main():
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
